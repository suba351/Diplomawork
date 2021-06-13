import sys
import Koshi_mu_xi2
print(sys.path)
import matplotlib.pyplot as plt
from functools import partial
from concurrent.futures import as_completed, ProcessPoolExecutor
import numpy as np
import time
A = np.load(r"/home/hello/PycharmProjects/NIR_/A_Matrix.npy", allow_pickle=True)
B = np.load(r"/home/hello/PycharmProjects/NIR_/B_Matrix.npy", allow_pickle=True)
D = np.load(r"/home/hello/PycharmProjects/NIR_/D_Matrix.npy", allow_pickle=True)


mx, Mx, nPtx = 0, 1.0, 32
my, My, nPty = 0, 0.5, 32
m_mu, M_mu, nPt_mu = 0.0, 0.15, 21

step_x = (Mx - mx) / nPtx / 2
step_y = (My - my) / nPty / 2
step_mu = (M_mu - m_mu) / nPt_mu / 2
xi_1 = 0.2

xi1_args = np.linspace(mx + step_x, Mx - step_x, nPtx)
xi2_args = np.linspace(my + step_y, My - step_y, nPty)
mu_args = np.linspace(m_mu, M_mu, nPt_mu)

plt.show()


def plot_dots(Matrix):
    x_space = np.linspace(mx, Mx, nPtx)
    y_space = mu_args
    plt.figure('graph')
    plt.xlim(mx-step_x, Mx+step_x)
    plt.ylim(m_mu-step_mu, M_mu+step_mu)
    plt.grid(True)
    plt.xlabel('xi_2', fontsize=12)
    plt.ylabel('mu', fontsize=12)
    plt.title('xi_1 =' + str(xi_1), fontsize=12)
    for x in range(nPty):
        for y in range(nPt_mu):
            if Matrix[x, y] == 1:
                plt.plot(x_space[x], y_space[y], 'o-r')
    plt.savefig(r'/home/hello/PycharmProjects/NIR_/figures_mu/' + 'xi1 = ' + str('{:.3f}'.format(xi_1)) + '.jpg')
    plt.show()


def define_stability_async(A, B, D, xi1,  *, n_jobs):
    executor = ProcessPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, Koshi_mu_xi2.define_stability, A, B, D, xi1)
    step = (Mx - mx) / n_jobs
    fs = [spawn(np.linspace(mx + step_x + i*step, mx + step_x + (i+1)*step, nPtx // n_jobs),
                mu_args)
          for i in range(n_jobs)]
    T = [f.result() for f in fs]
    print(T)
    Matr = T[0]
    for i in range(1, n_jobs):
        Matr = np.row_stack((Matr, T[i]))
    return Matr


if __name__ == '__main__':
    print("начали")
    xi1_args, xi2_args = np.linspace(mx + step_x, Mx - step_x, nPtx), np.linspace(my + step_y, My - step_y, nPty)
    start_time = time.time()
    M = define_stability_async(A, B, D, np.array((xi_1,)), n_jobs=8)
    print("--- %s seconds ---" % (time.time() - start_time))
    plot_dots(M)