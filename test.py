# Import the extension module hello.
import Koshi_last
import numpy as np

A = np.load(r"/home/hello/PycharmProjects/NIR_/A_Matrix.npy", allow_pickle=True)
B = np.load(r"/home/hello/PycharmProjects/NIR_/B_Matrix.npy", allow_pickle=True)
D = np.load(r"/home/hello/PycharmProjects/NIR_/D_Matrix.npy", allow_pickle=True)

etta, T = Koshi_last.etta(0.1, 0.2)
for i in range(40):
    print(etta(0.01 * i))
print(T)
