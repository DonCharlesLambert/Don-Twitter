from data import verses, quotes, investing, bad_word, good_word
from stock import random_stock, Stock
import random

def say_quote():
    return quotes[random.randint(0, len(quotes)-1)]

def say_verse():
    return verses[random.randint(0, len(verses)-1)]

def discuss_investing():
    stock = random_stock()
    price = stock.get_recent_price()
    yesterday_price = stock.get_yesterdays_price()
    difference = round(float(price)-float(yesterday_price), 2)

    speech = investing[random.randint(0, len(investing)-1)]
    speech = speech.replace("[[name]]", stock.name)
    speech = speech.replace("[[emoji]]", stock.emoji)
    speech = speech.replace("[[price]]", '£' + price)
    speech = speech.replace("[[raw_change]]", '£' + str(difference))
    speech = speech.replace("[[yesterday]]", yesterday_price)

    if difference > 0:
        speech = speech.replace("[[up]]", 'up')
    else:
        speech = speech.replace("[[up]]", 'down')

    if difference > 0:
        speech = speech.replace("[[description]]", good_word())
    else:
        speech = speech.replace("[[description]]", bad_word())

    return speech.capitalize()

print(say_verse())




