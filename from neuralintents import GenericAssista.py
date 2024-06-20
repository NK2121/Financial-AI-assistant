from neuralintents import GenericAssistant
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import mplfinance as mpf

import pickle
import sys
import datetime as dt
portfolio={'A':20, 'B':5 , 'C':30}
with open ('portfolio.pkl', 'wb') as f:
    pickle.dump(portfolio, f)
    
