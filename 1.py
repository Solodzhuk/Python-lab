import matplotlib.pyplot as plt

MAX_SIZE = 7 #inches

for num in range(5):
    with open(f"dead_moroz/00{num + 1}.dat") as f:
        n = int(f.readline())
        s_data = [[], []]
        for i in range(n):
            a, b = f.readline().split(" ")
            s_data[0].append(float(a))
            s_data[1].append(float(b))
        delta_x = max(s_data[0]) - min(s_data[0])
        delta_y = max(s_data[1]) - min(s_data[1])

        fig, ax = plt.subplots()

        if delta_x > delta_y:
            fig.set_size_inches(MAX_SIZE, MAX_SIZE*delta_y/delta_x)
        else:
            fig.set_size_inches(MAX_SIZE*delta_x/delta_y, MAX_SIZE)

        ax.scatter(s_data[0], s_data[1])
        plt.show()
