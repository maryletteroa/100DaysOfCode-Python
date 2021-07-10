import smtplib
import datetime as dt
from random import choice, randint
import pandas as pd

# create a dictionary of bday infos
df = pd.read_csv("./birthdays.csv", header=0)
bdays = { (row.month, row.day): row for (index,row) in df.iterrows()}


MY_EMAIL = "test@gmail.com"
PASSWORD = "abc123()"
SMTP = "smtp.gmail.com"
now = dt.datetime.now()

# check if current date is a birthdate
if (now.month, now.day) in bdays:
    bday = bdays[(now.month, now.day)]
    name = bday["name"]
    to_email = bday.email

    # select a random letter
    filename = f"./letter_templates/letter_{randint(1,3)}.txt"
    with open(filename) as file:
        greeting = file.read().replace("[NAME]", name)

    # email
    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendemail(
            from_addr=MY_EMAIL, 
            to_addrs=to_email, 
            msg=f"Subject:Happy Birthday!\n\n{greeting}"
        )
    



