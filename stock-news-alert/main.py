import requests
import datetime as dt
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_api_key = os.environ.get("STOCK_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,
}
news_params = {
    "apiKey": news_api_key,
    "qInTitle": COMPANY_NAME,

}
date1 = dt.date.today() - dt.timedelta(days=2)
date2 = dt.date.today() - dt.timedelta(days=3)


response1 = requests.get(STOCK_ENDPOINT,params=stock_params)
stock_data = response1.json()

yesterday_close = float(stock_data["Time Series (Daily)"][f"{date1}"]["4. close"])
db_yesterday_close = float(stock_data["Time Series (Daily)"][f"{date2}"]["4. close"])

change_percentage = (yesterday_close - db_yesterday_close)/db_yesterday_close * 100

if change_percentage > 5 or change_percentage < -5:
    response2 = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = response2.json()["articles"]
    three_articles = articles[:3]



    formatted_articles = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="twilio-number",
            to="YOUR NUMBER",
        )

