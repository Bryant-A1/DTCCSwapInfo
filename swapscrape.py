import pandas as pd

df = pd.read_html('http://www.dtcc.com/repository-otc-data/top-1000-single-names-06-20-2017-through-09-19-2017')

df[0]

df = df[0]

df.head() 