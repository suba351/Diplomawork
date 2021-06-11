import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
from sympy import symbols
from sympy import Symbol, re, sqrt
from sympy.solvers import solve
import os
from Plate.SubsValues import subs_values
p = Symbol("p")
xi1__, xi2__ = symbols('xi1__ xi2__', real=True)

M, C, F, b_a, f0_kappa0 = subs_values()


def print_freq(i, xi, mesh, p1, p2, p3):
    fig, axs = plt.subplots(3, 1, constrained_layout=True, figsize=(6, 9))
    axs[0].plot(mesh, p1, 'g', linewidth=2)
    axs[0].set_title('p1')
    axs[0].set_xlabel('xi_2')
    axs[0].set_ylabel('frequent')
    axs[0].grid(True)
    axs[0].yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    fig.suptitle('xi1 = ' + str('{:.3f}'.format(xi)), fontsize=16)

    axs[1].plot(mesh, p2, 'r', linewidth=2)
    axs[1].set_title('p2')
    axs[1].set_xlabel('xi_2')
    axs[1].set_ylabel('frequent')
    axs[1].yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    axs[1].grid(True)

    axs[2].plot(mesh, p3, 'b', linewidth=2)
    axs[2].set_title('p2')
    axs[2].set_xlabel('xi_2')
    axs[2].set_ylabel('frequent')
    axs[2].yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    axs[2].grid(True)
    plt.savefig(str(int(i)) + '. xi1 = ' + str('{:.3f}'.format(xi)) + '.jpg')
    plt.close()


def plot_grapghs(n_px=21, n_py=201):
    # разбиваем пластину сеткой (точки контакта)
    mesh1 = np.linspace(0.0, 1.0, n_px)
    mesh2 = np.linspace(0., b_a, n_py)
    os.chdir(r"/home/hello/PycharmProjects/NIR_/figures")
    i = 0

    for xi1 in mesh1:
        i += 1
        p1 = []
        p2 = []
        p3 = []
        С1 = C.subs(xi1__, xi1)
        for xi2 in mesh2:
            sol = solve((С1.subs(xi2__, xi2) - p * M).det(), p)
            p1.append(sqrt(re(sol[0])))
            p2.append(sqrt(re(sol[1])))
            p3.append(sqrt(re(sol[2])))
        print_freq(i, xi1, mesh2, p1, p2, p3)


plot_grapghs()
