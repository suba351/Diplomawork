from scipy.integrate import odeint
import matplotlib.pyplot as plt
from sympy import symbols, Matrix
from Plate.SubsValues import subs_values, subs_values_no_force
import numpy as np
from matplotlib import animation

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


etta_0, f1_0, f2_0 = -0.1, 0., 0.
detta_0, df1_0, df2_0 = 0., 0., 0.
y0 = [etta_0, detta_0, f1_0, df1_0, f2_0, df2_0]
t = np.linspace(0, 6, 10001)
result = odeint(system, y0, t)


def animations(result, l=0, r=1000, step=10):
    fig = plt.figure()
    ax = plt.axes(xlim=(t[l], t[r]), ylim=(-0.2, 0.2))
    ax.grid()
    plt.title('etta_0 = ' + str(etta_0) + '; ' + 'f1_0 = ' + str(f1_0) + '; ' + 'f2_0 = ' + str(f2_0))
    lines = [plt.plot([], [], 'b', label='etta(t)')[0], plt.plot([], [], 'g', label='f1(t)')[0], plt.plot([], [], 'r', label='f2(t)')[0]]
    legend = plt.legend(loc='best')
    patches = lines

    def init():
        lines[0].set_data([], [])
        lines[1].set_data([], [])
        lines[2].set_data([], [])
        return patches

    def animate(i):
        for j, line in enumerate(lines):
            line.set_data(t[step*i:r + step*i] - t[step*i], result[step*i:r + step*i, 2*j])
        return patches

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=1000, interval=10, blit=True)

    # anim.save('animation.gif', writer='PillowWriter', fps=20)
