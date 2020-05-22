import pandas as pd
import re

data = pd.read_csv("example.csv")
print(data)

def replace_ss(row):
	x = row['penntree']
	print('o',x)
	ss=str(row['sentiment_score'])
	x = re.sub(r'\d', r''+ss+'', x, count=1)
	# idx = re.search(r"\d", x)
	# x[idx] = str(row['sentiment_score'])
	print('n',x)
	row['penntree'] = x
	return row

ndata = data.apply(lambda row: replace_ss(row), axis=1)
