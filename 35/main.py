import requests
import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient


# commented lines for PythonAnywhere

MY_LAT = 14.599512
MY_LONG = 120.984222
OWM_KEY = os.environ.get("OWM_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
DESTINATION_NUMBER = os.environ.get("DESTINATION_NUMBER")

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"


weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": OWM_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
# first twelve-hours (7AM-7PM)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
# only print once
if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)#, http_client=proxy_client)
    message = client.messages \
        .create(
                body="It's going to rain today. Rember to bring an ☔",
                from_=TWILIO_NUMBER,
                to=DESTINATION_NUMBER,
            )
    print(message.status)