import requests
import keys
from data import stock_data

class Stock():
    def __init__(self, name):
        self.name = name
        self.symbol = stock_data[name][0]
        self.emoji = stock_data[name][1]

    def get_recent_price(self, time):
        response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={0}&interval='.format(self.symbol) + str(time) + 'min&outputsize=full&apikey={0}'.format(keys.ALPHAVANTAGE)).json()
        times = response['Time Series (' + str(time) + 'min)']
        most_recent_time = list(times.keys())[len(times.keys())-1]
        current_price_list = times[most_recent_time]
        return current_price_list['4. close']

    def get_recent_n_prices(self, n, time):
        response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={0}&interval='.format(self.symbol) + str(time) + 'min&outputsize=full&apikey={0}'.format(keys.ALPHAVANTAGE)).json()
        times = response['Time Series (' + str(time) + 'min)']
        prices = []
        for i in range(1, min(n+1, len(times.keys()))):
            ith_recent_time = list(times.keys())[len(times.keys())-i]
            price = times[ith_recent_time]['4. close']
            prices.append(price)
        return prices


apple = Stock('Apple')
print(apple.get_recent_n_prices(5, 15))