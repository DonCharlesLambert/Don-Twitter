import tweepy
import keys
import requests
import schedule
import random

def tweet(message):
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.update_status(message)
        print("Tweeted!")
    except Exception as e:
        print(e)

def get_recent_price(symbol):
    response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={1}&interval=15min&outputsize=full&apikey={0}'.format(keys.ALPHAVANTAGE, symbol))
    response = response.json()
    times = response['Time Series (15min)']
    most_recent_time = list(times.keys())[len(times.keys())-1]
    current_price_list = times[most_recent_time]
    return current_price_list['4. close']




def get_daily_tweet():
    stocks = {
        '\U0001F34E Apple'    : 'AAPL',
        '\U0001F3CE Tesla'    : 'TSLA',
        '\U0001F964 Coca-Cola': 'KO',
        '\U0001F9D1 Facebook' : 'FB',
        '\U0001F354 McDonalds': 'MCD',
        '\U0001F42D Disney'   : 'DIS',
    }
    
    tweet = 'Don is watching \n'
    for _ in range(3):
        name = list(stocks.keys())[random.randint(0, len(list(stocks.keys())) - 1)]
        symbol = stocks.pop(name)
        tweet += name + ': ' + get_recent_price(symbol) + '\n'
    return tweet

def tweet_up_message():
    tweet('\U0001F4BB Don is up')

def tweet_key_shares():
    msg = get_daily_tweet()
    tweet(msg)


schedule.every().day.at("08:30").do(tweet_up_message)
schedule.every(15).minutes.do(tweet_key_shares)

tweet_key_shares()
while True:
    schedule.run_pending()