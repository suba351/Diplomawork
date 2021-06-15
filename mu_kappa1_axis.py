import sys
import Koshi_mu_kappa1
print(sys.path)
import matplotlib.pyplot as plt
from functools import partial
from concurrent.futures import as_completed, ProcessPoolExecutor
import numpy as np
import time
A = np.load(r"/home/hello/PycharmProjects/NIR_/A_Matrix.npy", allow_pickle=True)
B = np.load(r"/home/hello/PycharmProjects/NIR_/B_Matrix.npy", allow_pickle=True)
D = np.load(r"/home/hello/PycharmProjects/NIR_/D_Matrix.npy", allow_pickle=True)


m_mu, M_mu, nPt_mu = 0.0, 4.0, 21
m_kappa1, M_kappa1, nPt_kappa1 = 0.0, 100000.0, 32

step_mu = (M_mu - m_mu) / nPt_mu / 2
step_kappa1 = (M_kappa1 - m_kappa1) / nPt_kappa1 / 2
xi_1 = 0.2
xi_2 = 0.3


mu_args = np.linspace(m_mu, M_mu, nPt_mu)
kappa1_args = np.linspace(m_kappa1, M_kappa1, nPt_kappa1)

plt.show()


def plot_dots(Matrix):
    x_space = kappa1_args
    y_space = mu_args
    plt.figure('graph')
    plt.xlim(m_kappa1 - step_kappa1, M_kappa1 + step_kappa1)
    plt.ylim(m_mu-step_mu, M_mu+step_mu)
    plt.grid(True)
    plt.xlabel('kappa1', fontsize=12)
    plt.ylabel('mu', fontsize=12)
    plt.title('xi_1 =' + str(xi_1) + 'xi_2 =' + str(xi_2), fontsize=12)
    for x in range(nPt_kappa1):
        for y in range(nPt_mu):
            if Matrix[x, y] == 1:
                plt.plot(x_space[x], y_space[y], 'o-r')
    plt.savefig(r'/home/hello/PycharmProjects/NIR_/figures_mu/' + 'xi1 = ' + str('{:.3f}'.format(xi_1)) + 'xi2 = ' + str('{:.3f}'.format(xi_2)) + '.jpg')
    plt.show()


def define_stability_async(A, B, D, xi1, xi2, *, n_jobs):
    executor = ProcessPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, Koshi_mu_kappa1.define_stability, A, B, D, xi1, xi2)
    step = (M_kappa1 - m_kappa1) / n_jobs
    fs = [spawn(np.linspace(m_kappa1 + step_kappa1 + i * step, m_kappa1 + step_kappa1 + (i + 1) * step, nPt_kappa1 // n_jobs),
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
    start_time = time.time()
    M = define_stability_async(A, B, D, np.array((xi_1,)), np.array((xi_2,)), n_jobs=8)
    print("--- %s seconds ---" % (time.time() - start_time))
    plot_dots(M)