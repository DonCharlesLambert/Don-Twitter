import tweepy
import keys
import schedule
import random

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

'''
schedule.every().day.at("08:30").do(tweet_up_message)
schedule.every(15).minutes.do(tweet_key_shares)
'''

while True:
    schedule.run_pending()