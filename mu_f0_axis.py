import sys
import Koshi_mu_f0
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
m_mu, M_mu, nPt_mu = 0.0, 1.0, 21
m_f0, M_f0, nPt_f0 = 0.0, 1.0, 32

step_x = (Mx - mx) / nPtx / 2
step_y = (My - my) / nPty / 2
step_mu = (M_mu - m_mu) / nPt_mu / 2
step_f0 = (M_f0 - m_f0) / nPt_f0 / 2
xi_1 = 0.2
xi_2 = 0.3

xi1_args = np.linspace(mx + step_x, Mx - step_x, nPtx)
xi2_args = np.linspace(my + step_y, My - step_y, nPty)
mu_args = np.linspace(m_mu, M_mu, nPt_mu)
f0_args = np.linspace(m_f0, M_f0, nPt_f0)

plt.show()


def plot_dots(Matrix):
    x_space = f0_args
    y_space = mu_args
    plt.figure('graph')
    plt.xlim(m_f0 - step_f0, M_f0 + step_f0)
    plt.ylim(m_mu-step_mu, M_mu+step_mu)
    plt.grid(True)
    plt.xlabel('f0', fontsize=12)
    plt.ylabel('mu', fontsize=12)
    plt.title('xi_1 =' + str(xi_1) + 'xi_2 =' + str(xi_2), fontsize=12)
    for x in range(nPt_f0):
        for y in range(nPt_mu):
            if Matrix[x, y] == 1:
                plt.plot(x_space[x], y_space[y], 'o-r')
    plt.savefig(r'/home/hello/PycharmProjects/NIR_/figures_mu/' + 'xi1 = ' + str('{:.3f}'.format(xi_1)) + 'xi2 = ' + str('{:.3f}'.format(xi_2)) + '.jpg')
    plt.show()


def define_stability_async(A, B, D, xi1, xi2, *, n_jobs):
    executor = ProcessPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, Koshi_mu_f0.define_stability, A, B, D, xi1, xi2)
    step = (M_f0 - m_f0) / n_jobs
    fs = [spawn(np.linspace(m_f0 + step_f0 + i*step, m_f0 + step_f0 + (i+1)*step, nPt_f0 // n_jobs),
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