import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = os.environ["STOCK_API_KEY"]
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
    "outputsize": "compact",
}

NEWS_API_KEY = os.environ["NEWS_API_KEY"]
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_data = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = abs(yesterday_closing_data - day_before_yesterday_closing_price)
diff_percent = (difference / yesterday_closing_data) * 100

if diff_percent > 1:
    news_params = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME,

    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)


