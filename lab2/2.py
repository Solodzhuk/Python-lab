import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("flights.csv", index_col=0)
print(data.groupby('CARGO').PRICE.count().keys())
print(data.groupby('CARGO').PRICE.sum())
print(data.groupby('CARGO').WEIGHT.sum())
fig, axs = plt.subplots(nrows=1, ncols=3)
fig.tight_layout()
axs[0].bar(data.groupby('CARGO').PRICE.count().keys(), data.groupby('CARGO').PRICE.count())
axs[1].bar(data.groupby('CARGO').PRICE.sum().keys(), data.groupby('CARGO').PRICE.sum())
axs[2].bar(data.groupby('CARGO').WEIGHT.sum().keys(), data.groupby('CARGO').WEIGHT.sum())
axs[0].title.set_text("count")
axs[1].title.set_text("price")
axs[2].title.set_text("cargo")
plt.show()