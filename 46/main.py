from warnings import resetwarnings
from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")


# get the top 100 songs
date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
response.raise_for_status
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

songs = soup.find_all(name="span", class_="chart-element__information__song")
artists = soup.find_all(name="span", class_="chart-element__information__artist")
song_titles = [song.getText() for song in songs]
artist_names = [artist.getText() for artist in artists]
tracks = zip(song_titles, artist_names)

# for track in tracks:
#     print(track[0], track[1])

# access spotify
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID, 
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri = "https://example.com/callback/",
        show_dialog = True,
        cache_path="token.txt",
        scope=scope)
    )
user_id = sp.current_user()["id"]

uris = []
for track in tracks:
    # search for the songs
    song, artist = track
    result = sp.search(f"artist:{artist} track:{song}", limit=1, type="track")
    hits = result["tracks"]["items"]
    if len(hits) == 0:
        print(f"{song} by {artist} is not available in Spotify")
    else:
        uri = hits[0]["uri"]
        uris.append(uri)

# create a playlist
playlist = sp.user_playlist_create(user_id, 
    f"{date} Bilboard 100", 
    public=False, 
    description= f"Top songs in {date}"
)
print(f"Playlist '{date} Bilboard 100' created.")

# add songs
playlist_id = playlist["id"]
external_urls = playlist["external_urls"]["spotify"]
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=uris)
print(f"{len(uris)} songs added.")
print(f"Access the playlist here: {external_urls}")