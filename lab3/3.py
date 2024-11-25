import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


a = np.loadtxt('data.txt')
l = len(a)
A = np.zeros((l, l))
A[np.arange(l), np.arange(l)] = 1
A[np.arange(l), (np.arange(l) - 1)] = -1

print(A)

fig = plt.figure()
ax = plt.axes(xlim=(0, l), ylim=(0, 10))
line, = ax.plot([], [], lw=3)


def init():
    line.set_data([], [])
    return line,

a_values = [a.copy()]

def animate(i):
    if i > 0:
        t = np.dot(A, a_values[-1])
        next_a = a_values[-1] - 0.5 * t
        a_values.append(next_a)
    else:
        next_a = a_values[0]

    x = np.linspace(0, l, l)
    y = next_a
    line.set_data(x, y)
    return line,


anim = FuncAnimation(fig, animate, init_func=init, frames=255, interval=20, blit=True)


anim.save('anim.gif', writer='imagemagick', fps=30)
