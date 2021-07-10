import requests
from datetime import datetime, time
import smtplib
import time

MY_LAT = 14.599512
MY_LONG = 120.984222
MY_EMAIL = "test@gmail.com"
PASSWORD = "abc123()"
SMTP = "smtp.gmail.com"

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
while True:
    time.sleep(60) # wait a minute before running the rest
    if is_iss_overhead() and is_night():
        with smtplib.SMTP(SMTP) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendemail(
                from_addr=MY_EMAIL, 
                to_addrs=MY_EMAIL, 
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky!"
            )
            