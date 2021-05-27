from beam.KOSHI_matrix import Koshi
import matplotlib.pyplot as plt
import numpy as np
import time
from sympy import Matrix, symbols, cos, sin
from scipy.integrate import odeint
Eps_multipliers = 0.001
N = 1000
n = 4


a, T = Koshi()

mx, Mx, nPtx = 0, 1.0, 10
my, My, nPty = 0, 0.5, 10
step_x = (Mx - mx) / nPtx / 2
step_y = (My - my) / nPty / 2


def plot_dots(Matrix):
    x_space = np.linspace(mx + step_x, Mx - step_x, nPtx)
    y_space = np.linspace(my + step_y, My - step_y, nPty)
    plt.figure('graph')
    plt.xlim(mx-step_x, Mx+step_x)
    plt.ylim(my-step_y, My+step_y)
    plt.grid(True)
    plt.xlabel('P[1]', fontsize=12)
    plt.ylabel('P[2]', fontsize=12)
    plt.title('graph', fontsize=12)
    for x in range(nPtx):
        for y in range(nPty):
            if Matrix[x, y] == 1:
                plt.plot(x_space[x], y_space[y], 'o-r')
    plt.show()


def define_stability(mu, xi_1_args, xi_2_args):
    start_time = time.time()

    StMatr = np.zeros((len(xi_1_args), len(xi_2_args)))
    for xi_1_iter, xi_1 in enumerate(xi_1_args):
        for xi_2_iter, xi_2 in enumerate(xi_2_args):
            TT = np.linspace(0, T, N + 1)
            h2 = T / N / 2
            A_matr = Koshi(mu, xi_1, xi_2)[0]
            A = A_matr(TT[0]) * h2
            I = np.eye(n, n)
            Monodromy = I
            for t in TT[1:]:
                B = A_matr(t) * h2
                Monodromy = (np.linalg.inv(I-B)).dot((I+A).dot(Monodromy))
                A = B
            multipliers = np.linalg.eig(Monodromy)[0]
            rho_max = max(list(map(abs, multipliers)))
            if rho_max > 1 + Eps_multipliers:
                StMatr[xi_1_iter, xi_2_iter] = 1

    print("--- %s seconds ---" % (time.time() - start_time))
    return StMatr


xi_1_args, xi_2_args = np.linspace(mx + step_x, Mx - step_x, nPtx), np.linspace(my + step_y, My - step_y, nPty)

define_stability(0.2, xi_1_args, xi_2_args)

plot_dots(define_stability(0.2, xi_1_args, xi_2_args))
