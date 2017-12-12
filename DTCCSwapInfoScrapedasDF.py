import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_html('http://www.dtcc.com/repository-otc-data/top-1000-single-names-06-20-2017-through-09-19-2017')

df[0]

df = df[0]

df.head()

# change headers by df.ix
# headers / column labels are labeled as 0, 1, 2, 3, etc.

#*Needs fixing*#

df.rename(columns={'REFERENCE ENTITY': '0', 'REGION': '1','INDEX CONSTITUENT': '2',  'TOTAL NUMBER OF CLEARING DEALERS': '3',
    'AVERAGE MONTHLY CLEARING DEALERS': '4','AVERAGE DAILY NOTIONAL (USD EQ)': '5', 'AVERAGE NUMBER TRADES/DAY': '6',
    'DOC CLAUSE %': '7'
}, inplace=True)


df.plot.bar(x=1, y=6)

#*Needs fixing*#
