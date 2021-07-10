import smtplib
import datetime as dt
from random import choice

MY_EMAIL = "test@gmail.com"
PASSWORD = "abc123()"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0: # weekday 0 is Monday
    with open("./quotes.txt") as file:
        all_quotes = file.readlines()
        quote = choice(all_quotes)
        print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendemail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL, 
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
