#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
import keys
import requests
import schedule
import sys

def tweet(message):
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.update_status(message)
        print("Tweeted! ")
    except:
        print("Error during authentication")

def get_recent_price(symbol):
    response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={1}&interval=60min&outputsize=full&apikey={0}'.format(keys.ALPHAVANTAGE, symbol))
    response = response.json()
    times = response['Time Series (60min)']
    most_recent_time = list(times.keys())[len(times.keys())-1]
    current_price_list = times[most_recent_time]
    return current_price_list['4. close']


def get_daily_tweet():
    tweet = 'Don is watching' + '\n' + '🍎 Apple: ' + get_recent_price('AAPL') + '\n' + '🏎️ Tesla: ' + get_recent_price('TSLA') + '\n' + '🥤 Coca-Cola: ' + get_recent_price('KO')
    return tweet

def tweet_key_shares():
    msg = get_daily_tweet()
    tweet(msg)


# schedule.every().day.at("18:30").do(tweet_key_shares)
schedule.every(15).minutes.do(tweet_key_shares)

tweet('💻 Don is up')
while True:
    schedule.run_pending()
print(sys.getdefaultencoding())