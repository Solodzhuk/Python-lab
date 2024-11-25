import numpy as np
import matplotlib.pyplot as plt


def func(data_in):
    sum = np.cumsum(data_in, dtype=float)
    sum[10:] = sum[10:] - sum[:-10]
    return sum / np.minimum(np.arange(1, len(data_in) + 1), 10)

fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(6, 12))
for i in range(3):
    data = np.loadtxt(f"signals/signal0{i + 1}.dat")
    new_data = func(data)
    axs[i][0].plot(data)
    axs[i][1].plot(new_data)
    axs[i][0].set_title(f"Сырой сигнал {i + 1}")
    axs[i][1].set_title(f"После фильтра {i + 1}")
    axs[i][0].grid(True)
    axs[i][1].grid(True)

plt.tight_layout()
plt.show()
