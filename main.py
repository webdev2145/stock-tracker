import requests
from pprint import pprint
from twilio.rest import Client
import lxml

from twilio_credentials import *
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}


responses = requests.get(STOCK_ENDPOINT, stock_parameters)

data = responses.json()

yesterday_closing_stock_price = float(data['Time Series (Daily)']['2020-12-18']['4. close'])

day_before_yesterday_closing_stock_price = float(data['Time Series (Daily)']['2020-12-17']['4. close'])

difference_between_stocks = abs(yesterday_closing_stock_price - day_before_yesterday_closing_stock_price)

percentage_increase = (difference_between_stocks / day_before_yesterday_closing_stock_price) * 100

if percentage_increase > 5:
    news_params = {
        'q': STOCK_NAME,
        'apiKey': STOCK_NEWS_API_KEY
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)

    news_data = news_response.json()

    first_three_articles = news_data["articles"][:3]

    news_title_description = [{"title": val["title"], "description": val['description']} for val in first_three_articles]
    # for n in news_title_description:
    #     n['title'] = n['title'].replace(u'\ax0', u' ')
    #     print(n)

    # print(news_title_description)
    output = ""
    for n in news_title_description:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_TOKEN)

        output += f"{STOCK_NAME}: {percentage_increase:2f}%\n \
                    Headline: {n['title']} \n \
                    Brief: {n['description']}\n"

        message = client.messages \
                        .create(
                                body=f"{output}",
                                from_="+17348022279",
                                to="18762766839"
                        )
        output = ""


# pprint(yesterday_closing_stock_price)
#
# print(difference_between_stocks)
#
# print(percentage_increase)
#

# ####Sources
# #Stocks data
#https://www.alphavantage.co/documentation/#daily