from bs4 import BeautifulSoup
import requests
import json

# Saves the top 100 movies of all time according to Empire in a file.
# Arranges movies from from 1) to 100)
# Check for any restrictions: https://www.empireonline.com/movies/features/best-movies-2/robots.txt

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

script = soup.find(name="script", id="__NEXT_DATA__").getText()
data = json.loads(script)
contents = data["props"]["pageProps"]["data"]["getArticleByFurl"]["_layout"][7]["content"]["images"]
titles = []
for content in contents:
    title_text = content["titleText"]
    if title_text[0].isnumeric() and (")" in title_text or ":" in title_text) :
        title = " ".join(title_text.split(" ")[1:])
    else:
        title = title_text
    titles.append(title)


with open("movies.txt","w")as file:
    print(f"Top {len(titles)} Greatest Movies", end="\n", file=file)
    for i, title in enumerate(titles[::-1]):
        print(f"{i+1}) {title}", end="\n", file=file)