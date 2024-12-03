import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

x = sp.symbols('x')
y = sp.Function('y')

dydx = -2 * y(x)
solution_sympy = sp.dsolve(sp.Eq(y(x).diff(x), dydx), y(x))

print("Символьное решение:", solution_sympy)

C1 = sp.symbols('C1')
y_value = sp.sqrt(2)
x_value = 0

C1_value = sp.solve(solution_sympy.subs({y(x): y_value, x: x_value}), C1)

print("Значение C1:", C1_value[0])

solution_sympy = solution_sympy.subs('C1', C1_value[0])
print("Решение задачи Коши с помощью sympy:", solution_sympy)

# ---- теперь с SciPy ----

def dydt(t, y):
    return -2 * y

y0 = np.sqrt(2)
Interval = (0, 10)
x_axis = np.linspace(Interval[0], Interval[1], 100)

solution = solve_ivp(dydt, Interval, [y0], t_eval=x_axis)

t_values = solution.t
y_values_scipy = solution.y[0]

y_solution = solution_sympy.rhs
y_numeric = sp.lambdify(x, y_solution, 'numpy') #преобразует функцию в численную для построения графика
y_values_sympy = y_numeric(x_axis)

dif=y_values_sympy-y_values_scipy

fig, axs = plt.subplots(1, 2,figsize=(12, 6))
axs[0].plot(x_axis, y_values_sympy, label='SymPy')
axs[0].scatter(t_values, y_values_scipy, label='SciPy', c='r')
axs[0].set_title("График решения ОДУ\n (они совпадают поэтому другой точками)")
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].axhline(0, color='black', lw=0.5, ls='--')
axs[0].axvline(0, color='black', lw=0.5, ls='--')
axs[0].legend()
axs[0].grid()

axs[1].plot(x_axis,dif)
axs[1].set_title('Различия в решениях уравнения методами SymPy и SciPy')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].axhline(0, color='black', lw=0.5, ls='--')
axs[1].axvline(0, color='black', lw=0.5, ls='--')
axs[1].grid()

plt.tight_layout()
plt.show()