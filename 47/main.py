import requests
from bs4 import BeautifulSoup
import lxml
import os
import smtplib

# skyward sword url
URL = "https://www.amazon.com/Legend-Zelda-Skyward-Sword-Nintendo-Switch/dp/B08WWFWRY6"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", "Accept-Language": "en-US,en;q=0.9"}
MY_EMAIL = os.environ.get("MY_EMAIL")
TO_EMAIL = os.environ.get("TO_EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

SMTP = os.environ.get("SMTP")

response = requests.get(URL, headers=HEADERS)
response.raise_for_status
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")
product_name = soup.find(name="span", id="productTitle").getText().strip()
price = float(soup.find(name="span", id="priceblock_ourprice").getText().split("$")[1])


if price <= 40:
    message=f"Subject:Amazon Price Alert!\n\n{product_name} is now ${price}\n{URL}"
    with smtplib.SMTP_SSL(SMTP, 465) as connection:
        # connection.starttls()
        # connection.ehlo()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=TO_EMAIL, 
            msg=message
        )