import matplotlib as mpl
import matplotlib.pyplot as plt
import math

data_x = []
data_y = []
max_x = 0.0
min_x = 0.0
max_y = 0.0
min_y = 0.0
with open("2.txt") as f:
    data = f.readlines()
    data_x = [data[i*2] for i in range(int(len(data)/2))]
    data_y = [data[i*2+1] for i in range(int(len(data)/2))]
    for g in range(len(data_x)):
        data_x[g] = [float(z) for z in data_x[g].split(" ")]
        data_y[g] = [float(z) for z in data_y[g].split(" ")]
        if min_x > min(data_x[g]):
            min_x = min(data_x[g])
        if min_y > min(data_y[g]):
            min_y = min(data_y[g])
        if max_x < max(data_x[g]):
            max_x = max(data_x[g])
        if max_y < max(data_y[g]):
            max_y = max(data_y[g])
    print(data)
    print(data_x)
    print(data_y)

count = len(data_x)

fig, axs = plt.subplots(nrows=math.ceil(count/2), ncols=2)
fig.tight_layout()
for i in range(count):
    axs[math.floor(i/2)][i%2].plot(data_x[i], data_y[i])
    axs[math.floor(i/2)][i%2].set_title(f"Frame {i}")
    axs[math.floor(i/2)][i%2].set_xlim(min_x - (max_x - min_x)*0.05, max_x + (max_x - min_x)*0.05)
    axs[math.floor(i/2)][i%2].set_ylim(min_y - (max_y - min_y)*0.1, max_y + (max_y - min_y)*0.1)
    axs[math.floor(i/2)][i%2].minorticks_on()
    axs[math.floor(i/2)][i%2].grid(which='both')
plt.show()