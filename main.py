import pandas as pd
import numpy as np

import yfinance as yf

import cufflinks as cf
cf.set_config_file(offline=True)

import warnings
warnings.filterwarnings('ignore')

print(pd.__version__, np.__version__, yf.__version__, cf.__version__)

df1 = yf.download('SPY', period='5d', progress=False)
print(df1.head())