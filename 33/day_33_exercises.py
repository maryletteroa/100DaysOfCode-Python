import requests
import json
from datetime import date, datetime

# --- ISS --- #
# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# # if response.status_code == 404:
# #     raise Exception("Resource does not exist.")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorized to access this data.")

# # instead of going over each HTTP codes
# response.raise_for_status()

# # get data from api
# data = response.json()["iss_position"]
# longitude = data["longitude"]
# latitude = data["latitude"]
# print(longitude, latitude)

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0, #24-hour clock
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise, sunset)
print(time_now.hour)