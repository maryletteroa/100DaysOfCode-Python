import requests
import os
from datetime import date
from twilio.rest import Client
from requests.api import head


perc_change = 0

# stock prices
def get_stock_price(stock_code):
    global perc_change
    URL = "https://www.alphavantage.co/query"
    API_KEY = os.environ.get("ALPHAVANTAGE_API")
    
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_code,
        "apikey": API_KEY,
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]

    today, yesterday = list(data.keys())[:2]
    close_price_today = float(data[today]["4. close"])
    close_price_yesterday = float(data[yesterday]["4. close"])

    difference = close_price_today - close_price_yesterday
    abs_perc_change = abs((difference / close_price_yesterday) * 100)
    
    perc_change = round(abs_perc_change, 2 )
    if perc_change > 0:
        symbol = "🔺[UP]" 
    elif perc_change < 0:
        symbol = "🔻[DOWN]"

    return f"{stock_code}: {symbol} {perc_change}%"

# news 
def get_news(company):
    API_KEY = os.environ.get("NEWS_API")
    URL = "https://newsapi.org/v2/everything"
    
    params = {
        "apiKey": API_KEY,
        "qInTitle": company,
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()

    news_list = []
    top_news = response.json()["articles"][:3]
    for news in top_news:
        headline = news["title"]
        # twilio does not send long messages
        # brief = news["description"]
        # news_list.append(f"""Headline: {headline}\nBrief: {brief}\n---""")
        news_list.append(f"""Headline: {headline}\n---""")
    
    return("\n".join(news_list))

if __name__ == "__main__":
    tesla_change = get_stock_price(stock_code="TSLA")
    tesla_news = get_news("Tesla")

    # send info if the percentage change is more than 5%
    if perc_change >= 5.0:
        TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
        TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
        TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
        DESTINATION_NUMBER = os.environ.get("DESTINATION_NUMBER")

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
                    body=f"{tesla_change}\n{tesla_news}",
                    from_=TWILIO_NUMBER,
                    to=DESTINATION_NUMBER,
                )
        print(message.body)
        print(message.status)

