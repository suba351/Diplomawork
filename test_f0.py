import Koshi_mu_xi2
import numpy as np
A = np.load(r"/home/hello/PycharmProjects/NIR_/A_Matrix.npy", allow_pickle=True)
B = np.load(r"/home/hello/PycharmProjects/NIR_/B_Matrix.npy", allow_pickle=True)
D = np.load(r"/home/hello/PycharmProjects/NIR_/D_Matrix.npy", allow_pickle=True)

print(Koshi_mu_xi2.Koshi(A, B, D, 0.2, 0.2, 0.2))
