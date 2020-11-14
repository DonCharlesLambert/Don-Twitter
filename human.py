from data import quotes
import random

def say_quote():
    return quotes[random.randint(0, len(quotes)-1)]



