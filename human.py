from data import verses, quotes, trading, investing, good_morning, bad_word, good_word, increased_word, decreased_word
from stock import random_stock, Stock
import random

def filter_speech(speech):
    stock = random_stock()
    price = round(float(stock.get_recent_price()), 2)
    yesterday_price = round(float(stock.get_yesterdays_price()), 2)
    prediction = round(float(stock.predict_share_price()), 2)
    difference = round(price-yesterday_price, 2)
    predict_change = round(prediction-price, 2)

    speech = speech.replace("[[name]]",         stock.name)
    speech = speech.replace("[[emoji]]",        stock.emoji)
    speech = speech.replace("[[price]]",        '£' + str(price))
    speech = speech.replace("[[raw_change]]",   '£' + str(difference))
    speech = speech.replace("[[pre_change]]",   '£' + str(predict_change))
    speech = speech.replace("[[yesterday]]",    '£' + str(yesterday_price))
    speech = speech.replace("[[predict]]",      '£' + str(prediction))

    if difference > 0:
        speech = speech.replace("[[up]]", 'up')
    else:
        speech = speech.replace("[[up]]", 'down')

    if difference > 0:
        speech = speech.replace("[[upe]]", '📈')
    else:
        speech = speech.replace("[[upe]]", '📉')

    if difference > 0:
        speech = speech.replace("[[description]]", good_word())
    else:
        speech = speech.replace("[[description]]", bad_word())
    
    if difference > 0:
        speech = speech.replace("[[increased]]", increased_word())
    else:
        speech = speech.replace("[[increased]]", decreased_word())
    
    if predict_change > 0:
        speech = speech.replace("[[pre_increase]]", 'increase')
    else:
        speech = speech.replace("[[pre_increase]]", 'decrease')

    if predict_change > 0:
        speech = speech.replace("[[upp]]", '📈')
    else:
        speech = speech.replace("[[upp]]", '📉')

    return speech[0].upper()+speech[1:]

def say_quote():
    return quotes[random.randint(0, len(quotes)-1)]

def say_verse():
    return verses[random.randint(0, len(verses)-1)]

def say_morning():
    return good_morning[random.randint(0, len(good_morning)-1)]

def discuss_investing():
    speech = investing[random.randint(0, len(investing)-1)]
    return filter_speech(speech)

def discuss_trading():
    speech = trading[random.randint(0, len(trading)-1)]
    return filter_speech(speech)


ss = random_stock()

def test_trading():
    for i in range(0, len(trading)-1):
        speech = trading[i]
        print(test_speech(speech))

def test_speech(speech):
    stock = ss
    price = round(float(stock.get_recent_price()), 2)
    yesterday_price = round(float(stock.get_yesterdays_price()), 2)
    prediction = round(float(stock.predict_share_price()), 2)
    difference = round(price-yesterday_price, 2)
    predict_change = round(prediction-price, 2)

    speech = speech.replace("[[name]]",         stock.name)
    speech = speech.replace("[[emoji]]",        stock.emoji)
    speech = speech.replace("[[price]]",        '£' + str(price))
    speech = speech.replace("[[raw_change]]",   '£' + str(difference))
    speech = speech.replace("[[pre_change]]",   '£' + str(predict_change))
    speech = speech.replace("[[yesterday]]",    '£' + str(yesterday_price))
    speech = speech.replace("[[predict]]",      '£' + str(prediction))

    if difference > 0:
        speech = speech.replace("[[up]]", 'up')
    else:
        speech = speech.replace("[[up]]", 'down')

    if difference > 0:
        speech = speech.replace("[[upe]]", '📈')
    else:
        speech = speech.replace("[[upe]]", '📉')

    if difference > 0:
        speech = speech.replace("[[description]]", good_word())
    else:
        speech = speech.replace("[[description]]", bad_word())
    
    if difference > 0:
        speech = speech.replace("[[increased]]", increased_word())
    else:
        speech = speech.replace("[[increased]]", decreased_word())
    
    if predict_change > 0:
        speech = speech.replace("[[pre_increase]]", 'increase')
    else:
        speech = speech.replace("[[pre_increase]]", 'decrease')

    if predict_change > 0:
        speech = speech.replace("[[upp]]", '📈')
    else:
        speech = speech.replace("[[upp]]", '📉')

    return speech[0].upper()+speech[1:]