from scipy.integrate import odeint
import matplotlib.pyplot as plt
from sympy import symbols, Matrix
from Plate.SubsValues import subs_values
import numpy as np
import time

xi1__, xi2__ = symbols('xi1__ xi2__', real=True)
M, C, F, b_a, f0_kappa0 = subs_values()
xi1, xi2 = 0.6, 0.3
M = M.subs([(xi1__, xi1), (xi2__, xi2)])
C = C.subs([(xi1__, xi1), (xi2__, xi2)])
F = F.subs([(xi1__, xi1), (xi2__, xi2)])
print(M)
print(C)
print(F)
vect = np.array(M.inv() * F)
matr = np.array(M.inv() * C)


def system(y, t):
    etta, d_etta, f1, d_f1, f2, d_f2 = y
    dydt = [d_etta, vect[0][0] - (matr[0][0]*etta + matr[0][1]*f1 + matr[0][2]*f2), d_f1, vect[1][0] - ((matr[1][0]*etta + matr[1][1]*f1 + matr[1][2]*f2)),d_f2, vect[2][0] - ((matr[2][0]*etta + matr[2][1]*f1 + matr[2][2]*f2))]
    return dydt


def system1(y, t):
    omega, theta = y
    dydt = [omega, -2*omega - 3*np.sin(theta)]
    return dydt


etta_0, f1_0, f2_0 = 0.0, 0.1, 0
y0 = [etta_0, 0.0, f1_0, 0.0, f2_0, 0.0]
t = np.linspace(0, 0.3, 10001)


result = odeint(system, y0, t)


plt.plot(t, result[:, 0], 'b', label='etta(t)')
plt.plot(t, result[:, 2], 'g', label='f1(t)')
plt.plot(t, result[:, 4], 'r', label='f2(t)')
plt.grid()
plt.title('etta_0 = ' + str(etta_0) + '; ' + 'f1_0 = ' + str(f1_0) + '; ' + 'f2_0 = ' + str(f2_0))
plt.legend(loc='best')
plt.xlabel('t')
plt.show()
