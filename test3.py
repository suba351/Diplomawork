import sys
import Koshi_last
print(sys.path)
import matplotlib.pyplot as plt
from functools import partial
from concurrent.futures import as_completed, ProcessPoolExecutor
import numpy as np
import time
A = np.load(r"/home/hello/PycharmProjects/NIR_/A_Matrix.npy", allow_pickle=True)
B = np.load(r"/home/hello/PycharmProjects/NIR_/B_Matrix.npy", allow_pickle=True)
D = np.load(r"/home/hello/PycharmProjects/NIR_/D_Matrix.npy", allow_pickle=True)

mu_args = np.linspace(0.0, 1.0, 11)
mx, Mx, nPtx = 0, 1.0, 32
my, My, nPty = 0, 0.5, 32
step_x = (Mx - mx) / nPtx / 2
step_y = (My - my) / nPty / 2

xi1_args, xi2_args = np.linspace(mx + step_x, Mx - step_x, nPtx), np.linspace(my + step_y, My - step_y, nPty)

plt.show()
def plot_dots(Matrix):
    x_space = np.linspace(mx, Mx, nPtx)
    y_space = mu_args
    plt.figure('graph')
    plt.xlim(mx-step_x, Mx+step_x)
    plt.ylim(mu_args[0], mu_args[-1])
    plt.grid(True)
    plt.xlabel('xi_2', fontsize=12)
    plt.ylabel('mu', fontsize=12)
    plt.title('graph', fontsize=12)
    for x in range(nPty):
        for y in range(11):
            if Matrix[x, y] == 1:
                plt.plot(x_space[x], y_space[y], 'o-r')
    plt.savefig(r'/home/hello/PycharmProjects/NIR_/figures_mu/' + str(1) + '. xi1 = ' + str('{:.3f}'.format(0.2)) + '.jpg')
    plt.show()

a = np.array([[0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1.]])

plot_dots(a)
a = input()
