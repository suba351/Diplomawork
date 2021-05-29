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
    plt.ylim(my-step_y, My+step_y)
    plt.grid(True)
    plt.xlabel('xi_2', fontsize=12)
    plt.ylabel('mu', fontsize=12)
    plt.title('graph', fontsize=12)
    for x in range(nPty):
        for y in range(11):
            if Matrix[x, y] == 1:
                plt.plot(x_space[x], y_space[y], 'o-r')
    plt.show()


def define_stability_async(A, B, D, coeffs, mu,  *, n_jobs):
    executor = ProcessPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, Koshi_last.define_stability, A, B, D, coeffs, mu)
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
    M = define_stability_async(A, B, D, np.array([0.2, 0.3]), np.array((0.2,)), n_jobs=8)
    print("--- %s seconds ---" % (time.time() - start_time))
    plot_dots(M)
    a = input()
