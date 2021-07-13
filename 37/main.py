import requests
import os
from datetime import datetime


TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = os.environ.get("PIXELA_USERNAME")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create user
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# -----# 

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Meditation Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# create a graph
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# -----# 

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today = datetime.now().strftime("%Y%m%d")
yesterday = datetime(year=2021, month=7, day=11).strftime("%Y%m%d")
pixel_config = {
    "date": today,
    "quantity": input("How many minutes did you meditate today? "),
}
# add a pixel
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# -----# 

yesterday = datetime(year=2021, month=7, day=11).strftime("%Y%m%d")
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"

new_pixel_data = {
    "date": today,
    "quantity": "25",
}
# modify a pixel
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

# -----# 

# delete a pixel
response = requests.delete(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# delete user
user_endpoint = f"{pixela_endpoint}/{USERNAME}"
response = requests.delete(url=user_endpoint, headers=headers)
print(response.text)

