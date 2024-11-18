import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_html("students/results_ejudge.html")[0]
info = pd.read_excel("students/students_info.xlsx", sheet_name='logins')
info = info.sort_values(by=['group_faculty'])
facs = set()
login_by_fac = [[]]
for i in range(len(info.group_faculty)):
    if not (info.group_faculty[i] in facs):
        facs.add(info.group_faculty[i])
        login_by_fac.append([])
    login_by_fac[info.group_faculty[i] - 1].append(info.login[i])
solved_by_fac = []
for i in range(len(facs)):
    solved_by_fac.append(data.loc[data.User.isin(login_by_fac[i])].Solved.sum())
fig, axs = plt.subplots(ncols=2)
axs[0].bar(list([str(i) for i in facs]), [int(i) for i in solved_by_fac])
axs[0].title.set_text("by fac")

info = info.sort_values(by='group_out')
groups = []
login_by_group = []
for i in range(len(info.group_out)):
    if not (info.group_out[i] in groups):
        groups.append(info.group_out[i])
        login_by_group.append([])
    login_by_group[list(groups).index(info.group_out[i])].append(info.login[i])
solved_by_group = []
for i in range(len(groups)):
    solved_by_group.append(data.loc[data.User.isin(login_by_group[i])].Solved.sum())
axs[1].bar(list([str(i) for i in groups]), [int(i) for i in solved_by_group])
axs[1].title.set_text("by group")
plt.show()

info = info.sort_values(by='group_faculty')
data1 = data.loc[(data.G >= 10) | (data.H >= 10)]
for i in data1.User:
    index = info.index[info['login'] == i].tolist()
    print("group_faculty",int(info.group_faculty[index].iloc[0]), "group_out", int(info.group_out[index].iloc[0]))