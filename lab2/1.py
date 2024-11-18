import pandas as pd

data = pd.read_csv("transactions.csv", index_col=0)
print("#1 top 3 payments\n", data.loc[data.STATUS == 'OK'].sort_values(by='SUM', ascending=False)[:3])
print("\n#2 Umbrella sum:", data.loc[(data.STATUS == 'OK') & (data.CONTRACTOR == 'Umbrella, Inc')].SUM.sum())