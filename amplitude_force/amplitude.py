from scipy.integrate import odeint
import matplotlib.pyplot as plt
from sympy import symbols, Matrix
from Plate.SubsValues import subs_values, subs_values_no_force
import numpy as np
from matplotlib import animation
import time

xi1__, xi2__ = symbols('xi1__ xi2__', real=True)
M, C, F, b_a, f0_kappa0_k0 = subs_values()
M_nf, C_nf, F_nf = subs_values_no_force()

xi1, xi2 = 0.5, 0.3
M = M.subs([(xi1__, xi1), (xi2__, xi2)])
C = C.subs([(xi1__, xi1), (xi2__, xi2)])
F = F.subs([(xi1__, xi1), (xi2__, xi2)])

M_nf = M_nf.subs([(xi1__, xi1), (xi2__, xi2)])
C_nf = C_nf.subs([(xi1__, xi1), (xi2__, xi2)])
F_nf = F_nf.subs([(xi1__, xi1), (xi2__, xi2)])


print(M)
print(C)
print(F)
vect_plus = np.array(M.inv() * F)
vect_minus = np.array(M_nf.inv() * F_nf)

matr_plus = np.array(M.inv() * C)
matr_minus = np.array(M_nf.inv() * C_nf)

u1 = np.load(r"F:\NIR_4th_semestr\U1.npy", allow_pickle=True)
u2 = np.load(r"F:\NIR_4th_semestr\U2.npy", allow_pickle=True)

u1 = u1[0].subs([(xi1__, xi1), (xi2__, xi2)])
u2 = u2[0].subs([(xi1__, xi1), (xi2__, xi2)])

print()
print(u1, u2)
print(f0_kappa0_k0)


def system(y, t):
    etta, d_etta, f1, d_f1, f2, d_f2 = y
    if etta - u1*f1 - u2*f2 + f0_kappa0_k0[2] > 0:
        return [d_etta, vect_plus[0][0] - (matr_plus[0][0] * etta + matr_plus[0][1] * f1 + matr_plus[0][2] * f2),
                d_f1, vect_plus[1][0] - (matr_plus[1][0] * etta + matr_plus[1][1] * f1 + matr_plus[1][2] * f2),
                d_f2, vect_plus[2][0] - (matr_plus[2][0] * etta + matr_plus[2][1] * f1 + matr_plus[2][2] * f2)]
    else:
        return [d_etta, vect_minus[0][0] - (matr_minus[0][0] * etta + matr_minus[0][1] * f1 + matr_minus[0][2] * f2),
                d_f1, vect_minus[1][0] - (matr_minus[1][0] * etta + matr_minus[1][1] * f1 + matr_minus[1][2] * f2),
                d_f2, vect_minus[2][0] - (matr_minus[2][0] * etta + matr_minus[2][1] * f1 + matr_minus[2][2] * f2)]


etta_0, f1_0, f2_0 = -0.03, 0., 0.
detta_0, df1_0, df2_0 = 0., 0., 0.
y0 = [etta_0, detta_0, f1_0, df1_0, f2_0, df2_0]
t = np.linspace(0, 1, 10001)


result = odeint(system, y0, t)

plt.figure('displacement')
plt.plot(t, result[:, 0], 'b', label='etta(t)')
plt.plot(t, result[:, 2], 'g', label='f1(t)')
plt.plot(t, result[:, 4], 'r', label='f2(t)')
plt.grid()
plt.title('etta_0 = ' + str(etta_0) + '; ' + 'f1_0 = ' + str(f1_0) + '; ' + 'f2_0 = ' + str(f2_0))
plt.legend(loc='best')
plt.xlabel('t')

plt.figure('force')
plt.plot(t, f0_kappa0_k0[1] * result[:, 0], 'b', label='T')
plt.grid()
plt.title('Force')
plt.legend(loc='best')
plt.xlabel('t')

plt.show()

