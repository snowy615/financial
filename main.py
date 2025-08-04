import pandas as pd
import numpy as np

import yfinance as yf

import cufflinks as cf
cf.set_config_file(offline=True)

import warnings
warnings.filterwarnings('ignore')

pd.__version__, cf.__version__, yf.__version__
