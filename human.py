from data import quotes
import random

def get_random_quote():
    return quotes[random.randint(0, len(quotes)-1)]

