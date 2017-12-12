# Fred Import
from fredapi import Fred
import pandas as pd

# Use your API Key, https://research.stlouisfed.org/docs/api/api_key.html
fred = Fred(api_key='YOUR API KEY HERE')

# Pulls all GDP releases into a dataframe
df = fred.get_series_all_releases('GDP')
df.tail()


# Plotting LIBOR Example
libor = fred.search_by_release(175, limit=5, order_by='popularity', sort_order='desc')
libor['title']
df = {}
df['percent'] = fred.get_series('USD3MTD156N')
df = pd.DataFrame(df)
df.plot()


# Searching for data on FRED, this will output a 15 row by 1000 column table
fred.search('gdp').T
