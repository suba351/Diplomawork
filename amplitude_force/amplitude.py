from scipy.integrate import odeint
import matplotlib.pyplot as plt
from sympy import symbols, Matrix
from Plate.SubsValues import subs_values
import numpy as np
import time

xi1__, xi2__ = symbols('xi1__ xi2__', real=True)
M, C, F, b_a, f0_kappa0 = subs_values()
xi1, xi2 = 0.1, 0.2
M = M.subs([(xi1__, xi1), (xi2__, xi2)])
C = C.subs([(xi1__, xi1), (xi2__, xi2)])
F = F.subs([(xi1__, xi1), (xi2__, xi2)])
print(M)
print(C)
print(F)
vect = M.inv() * F
matr = M.inv() * C
print(vect)
print(matr)


def system(y, t):
    etta, d_etta, f1, d_f1, f2, d_f2 = y
    dydt = [d_etta, float(vect[0] - (matr * Matrix(etta, f1, f2))[0]), d_f1, float(vect[1] - (matr * Matrix(etta, f1, f2))[1]), float(vect[2] - (matr * Matrix(etta, f1, f2))[2]), d_f2]
    return dydt


y0 = [0.1, 0, 0, 0, 0, 0]
t = np.linspace(0, 10, 10001)

result = odeint(system, y0, t)


plt.plot(t, result[:, 0], 'b', label='etta(t)')
plt.plot(t, result[:, 2], 'g', label='f1(t)')
plt.plot(t, result[:, 4], 'r', label='f2(t)')
plt.grid()
plt.legend(loc='best')
plt.xlabel('t')
plt.show()