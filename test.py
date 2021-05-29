# Import the extension module hello.
import Koshi_last
import numpy as np
A = np.load(r"/home/hello/PycharmProjects/NIR_/A_Matrix.npy", allow_pickle=True)
B = np.load(r"/home/hello/PycharmProjects/NIR_/B_Matrix.npy", allow_pickle=True)
D = np.load(r"/home/hello/PycharmProjects/NIR_/D_Matrix.npy", allow_pickle=True)

matrix, T = Koshi_last.Koshi(A, B, D, np.array([0.2, 0.3]), 0.2, 0.2, 0.2)
for i in range(40):
    print(matrix(0.01 * i))
print(T)
