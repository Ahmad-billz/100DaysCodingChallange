import requests
import config
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_KEY = config.s_key
NEWS_KEY = config.n_key

TWILIO_SID = config.t_sid
TWILIO_AUTH_TOKEN = config.t_at

s_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_KEY
}
s_response = requests.get(STOCK_ENDPOINT, params=s_parameters)
s_data = s_response.json()['Time Series (Daily)']
s_list = [value for (key, value) in s_data.items()]
yesterday_data = s_list[0]
yesterday_close = yesterday_data['4. close']


day_before_yesterday_data = s_list[1]
day_before_yesterday_close = day_before_yesterday_data['4. close']

change = float(yesterday_close) - float(day_before_yesterday_close)
up_down = None
if change > 0:
    up_down = '🔼'
else:
    up_down = '🔽'
difference_percentage = round((abs(change)/float(yesterday_close))*100)
if difference_percentage > 10:
    n_parameters = {
        'q': COMPANY_NAME,
        'from': '2021-03-15&',
        'sortBy': 'popularity&',
        'apiKey': NEWS_KEY
    }

    n_response = requests.get(NEWS_ENDPOINT, params=n_parameters)
    n_data = n_response.json()
    top_articles = n_data['articles'][:3]

    formatted_articles = [f"{STOCK}: {up_down} {difference_percentage}% \nHeadline: {article['title']}.\nBrief: {article['description']}" for article in top_articles]
    print(formatted_articles)
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=config.f_number,
            to=config.number
        )

