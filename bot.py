import tweepy
import keys
import schedule
import random
from human import say_morning, say_verse, say_quote, discuss_investing, discuss_trading

def tweet(message):
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.update_status(message)
        return True
    except:
        return False

def tweet_up_message():
    return tweet('\U0001F4BB Don is up')

def tweet_morning():
    return tweet(say_morning())

def tweet_verse():
    return tweet(say_verse())

def tweet_investing():
    return tweet(discuss_investing())

def tweet_trading():
    return tweet(discuss_trading())

def tweet_quote():
    return tweet(say_quote())

schedule.every().day.at("08:30").do(tweet_morning)
schedule.every(2).hours.do(tweet_verse)
# schedule.every().day.at("13:00").do(tweet_investing)
schedule.every().hour.do(tweet_trading)
schedule.every().day.at("18:00").do(tweet_quote)

tweet('John 3:16')
while True:
    schedule.run_pending()