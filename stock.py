import requests
import keys
from data import stock_data
import numpy as np
from sklearn import datasets, linear_model
import datetime

class Stock():
    def __init__(self, name):
        self.name = name
        self.symbol = stock_data[name][0]
        self.emoji = stock_data[name][1]
        self.times = self.get_times(15)

    def get_times(self, interval):
        response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={0}&interval='.format(self.symbol) + str(interval) + 'min&outputsize=full&apikey={0}'.format(keys.ALPHAVANTAGE)).json()
        times = response['Time Series (' + str(interval) + 'min)']
        return times

    def get_yesterdays_price(self):
        yesterday = datetime.datetime.now() - datetime.timedelta(1)
        yesterstring = datetime.datetime.strftime(yesterday, '%Y-%m-%d')
        response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={0}&apikey={1}'.format(self.symbol, keys.ALPHAVANTAGE)).json()
        times = response['Time Series (Daily)']
        yesterdays_prices = times[yesterstring]
        return yesterdays_prices['4. close']

    def get_recent_price(self):
        most_recent_time = list(self.times.keys())[len(self.times.keys())-1]
        current_price_list = self.times[most_recent_time]
        return current_price_list['4. close']

    def get_recent_n_prices(self, n):
        prices = []
        for i in range(1, min(n+1, len(self.times.keys()))):
            ith_recent_time = list(self.times.keys())[len(self.times.keys())-i]
            price = self.times[ith_recent_time]['4. close']
            prices.append(price)
        return prices

    def predict_share_price(self):
        y_train = np.array(self.get_recent_n_prices(5))
        x_train = np.array([i*15 for i in range(0, len(y_train))]).reshape((-1, 1))
        x_test = [x_train[len(x_train) - 1] + 15]
        # Create linear regression object
        regr = linear_model.LinearRegression()

        # Train the model using the training sets
        regr.fit(x_train, y_train)

        # Make predictions using the testing set
        y_pred = regr.predict(x_test)
        return y_pred

apple = Stock('Apple')
print(apple.get_yesterdays_price())