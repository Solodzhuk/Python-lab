import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import numpy as np

data = []
by_prep = {}
by_group = {}
with open("students.csv") as f:
    data_0 = f.readlines()
    for i in range(len(data_0)):
        data.append(data_0[i].split(";"))
        data[i][0] = str(data[i][0])
        data[i][1] = int(data[i][1])
        data[i][2] = int(data[i][2])
    prep_count = len(set([z[0] for z in data]))
    groups = sorted(set([z[1] for z in data]))
    for i in range(prep_count):
        by_prep[f"prep{i+1}"] = [0] * 10
    for i in groups:
        by_group[i] = [0] * 10
    for i in range(len(data)):
        arr = by_prep[(data[i])[0]]
        arr[(data[i])[2] - 1] += 1
        by_prep[(data[i])[0]] = arr
        arr = by_group[(data[i])[1]]
        arr[(data[i])[2] - 1] += 1
        by_group[(data[i])[1]] = arr
    print(by_group)

    by_prep_fr = {}
    by_group_fr = {}
    for i in range(10):
        by_prep_fr[i+1] = [by_prep[f"prep{z+1}"][i] for z in range(prep_count)]
        by_group_fr[i+1] = [by_group[z][i] for z in groups]
    print(by_group_fr)
    print(groups)
# -----------------------------------------------------------------------

    width = 0.5

    fig, axs = plt.subplots(nrows=2)
    fig.tight_layout()

    bottom = np.zeros(prep_count)

    for boolean, weight_count in by_prep_fr.items():
        p = axs[0].bar([f"prep{z}" for z in range(prep_count)], weight_count, width, label=boolean, bottom=bottom)
        bottom += weight_count
    axs[0].legend()
    print([f"prep{z}" for z in range(prep_count)])
    print(by_prep_fr.items())
    bottom = np.zeros(len(groups))
    print(by_group_fr.items())

    for boolean, weight_count in by_group_fr.items():
        print(1)
        z = axs[1].bar(groups, weight_count, width, label=boolean, bottom=bottom)
        bottom += weight_count
    axs[1].legend()
    plt.show()