import sys
import Koshi_last
print(sys.path)
sys.path.append('C:\\Users\\kirik\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages')
import matplotlib.pyplot as plt
from functools import partial
from concurrent.futures import as_completed, ProcessPoolExecutor
import numpy as np
import time
A = np.load(r"F:\NIR_4th_semestr\TEST\A_Matrix.npy", allow_pickle=True)
B = np.load(r"F:\NIR_4th_semestr\TEST\B_Matrix.npy", allow_pickle=True)
D = np.load(r"F:\NIR_4th_semestr\TEST\D_Matrix.npy", allow_pickle=True)
coeffs = [[119.70647156248701, 0.0010825618631403865, 0.0], [287.50279265854937, 0.02814203176239039, 0.0], [3128.8357316400056, 0.9999999994866093, 0.0]]
coeffs = np.array(coeffs)

mx, Mx, nPtx = 0, 1.0, 60
my, My, nPty = 0, 0.5, 60
step_x = (Mx - mx) / nPtx / 2
step_y = (My - my) / nPty / 2

xi1_args, xi2_args = np.linspace(mx + step_x, Mx - step_x, nPtx), np.linspace(my + step_y, My - step_y, nPty)
# start_time = time.time()
# print(Koshi_last.Koshi(A, B, D, coeffs)(0.1))
# print(type(Koshi_last.Koshi(A, B, D, coeffs)(0.1)))
# a = Koshi_last.define_stability(xi1_args, xi2_args, A, B, D, coeffs)
# print("--- %s seconds ---" % (time.time() - start_time))
# print(a)


def plot_dots(Matrix):
    x_space = np.linspace(mx, Mx, nPtx)
    y_space = np.linspace(my, My, nPty)
    step_x = (mx - Mx) / nPtx * 2
    step_y = (my - My) / nPty * 2
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


def define_stability_async(xi1_args, xi2_args, A, B, D, coeffs, *, n_jobs):
    executor = ProcessPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, Koshi_last.define_stability, xi1_args, xi2_args, A, B, D, coeffs)
    step = (Mx - mx) / n_jobs
    fs = [spawn(np.linspace(mx + i*step, mx + (i+1)*step, nPtx // n_jobs),
                np.linspace(my, My, nPty))
          for i in range(n_jobs)]
    T = [f.result() for f in fs]
    Matr = T[0]
    for i in range(1, n_jobs):
        Matr = np.row_stack((Matr, T[i]))
    return Matr


if __name__ == '__main__':
    print("начали")
    xi1_args, xi2_args = np.linspace(mx + step_x, Mx - step_x, nPtx), np.linspace(my + step_y, My - step_y, nPty)
    start_time = time.time()
    M = define_stability_async(xi1_args, xi2_args, A, B, D, coeffs, n_jobs=8)
    print("--- %s seconds ---" % (time.time() - start_time))
    plot_dots(M)
    a = input()
