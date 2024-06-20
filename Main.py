from neuralintents import GenericAssistant
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import mplfinance as mpf
import pickle
import sys
import datetime as dt
portfolio={'AAPL':20, 'TSLA':5 , 'GS':30  }
with open ('portfolio.pkl', 'rb') as f:
    portfolio=pickle.load( f)
def save_portfolio():
    with open ('portfolio.pkl', 'wb') as f:
        pickle.dump(portfolio, f)
def add_portfolio():
    ticker=input('The name of the stock')
    amount=input('The amount of stock to add to the portfolio')
    if ticker in portfolio.keys():
        portfolio[ticker]+=amount
    else:
        portfolio[ticker]=amount
    save_portfolio()
def remove_portfolio():
    ticker=input('The name of the stock')
    amount=input('The amount of stock to add to the portfolio')
    if ticker in portfolio.keys():
        if amount>portfolio[ticker]:
            print(' The amount is greater than the portfolio')
        else:
            portfolio[ticker]-=amount
    else:
        print('You dont own that Stonksssssssss lazy ass buy some stocks')
def show_portfolio():
    print (portfolio)
print (portfolio)