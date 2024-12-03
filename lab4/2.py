import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

with open('data.txt', 'r') as file:
    N = int(file.readline().strip())

    A = np.zeros((N, N))
    for i in range(N):
        row = list(map(float, file.readline().strip().split()))
        A[i] = row

    b = np.array(list(map(float, file.readline().strip().split())))

    x = linalg.solve(A, b)

    print("Решение СЛАУ: x =", x)
    print("Проверка решения: Ax - b =", A @ x - b)

    plt.bar(np.arange(len(x)), x)
    plt.title('Вектор решения СЛАУ')
    plt.grid()
    plt.show()