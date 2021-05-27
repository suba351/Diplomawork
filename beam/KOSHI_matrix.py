from sympy import symbols, Symbol, sqrt, Matrix
import numpy as np
from Plate.ReadData import read_data
from beam.DefineFunctionEtta import etta

values = read_data()
p0, D, N0, m0, V, A_len, l_len, E_len, a = symbols('p0 D N0 m0 V A_len l_len E_len a', real=True)
rho, h, mu_1, E = symbols('rho h mu E', real=True)

values[p0] = sqrt(values[D] / (values[rho] * values[h] * values[a] ** 4))
values[D] = values[E] * values[h] ** 3 / (12 * (1 - values[mu_1] ** 2))

f0 = values[N0] / (values[m0] * values[a]**2 * values[p0]**2)
kappa0 = values[E_len]*values[A_len] / (values[m0] * values[a] * values[p0]**2)

A = np.load(r"F:\NIR_4th_semestr\beam\A_Matrix.npy", allow_pickle=True)
B = np.load(r"F:\NIR_4th_semestr\beam\B_Matrix.npy", allow_pickle=True)
D = np.load(r"F:\NIR_4th_semestr\beam\D_Matrix.npy", allow_pickle=True)


def Koshi(mu=values[V] / (values[p0] * values[a]), xi_1=0.1, xi_2=0.2):
    etta_, T = etta(xi_1, xi_2)

    def Koshi_matrix(t):
        return np.array([
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [-(mu**2 - f0 - kappa0*etta_(t))*D[0][0]/A[0][0], 0, 0, -2*mu*B[0][1]/A[0][0]],
            [0, -(mu**2 - f0 - kappa0*etta_(t))*D[1][1]/A[1][1], -2*mu*B[1][0]/A[1][1], 0]
        ], dtype='float')

    return Koshi_matrix, T
