import cython
cimport cython
import numpy as np
cimport numpy as np
from libc.math cimport pi, cos, sin
from sympy import symbols, Matrix, Symbol, re, sqrt
from sympy.solvers import solve
from sympy.utilities.autowrap import autowrap
import os
os.chdir(r'/home/hello/PycharmProjects/NIR_')
from Plate.SubsValues import subs_values

t = Symbol('t')
p = Symbol('p')
xi1__, xi2__ = symbols('xi1__ xi2__', real=True)
M, C, F, b_a, f0_kappa0 = subs_values()
C_c = autowrap(C, args=(xi1__, xi2__), backend='cython', tempdir='./autowraptmp_C')
F_c = autowrap(F, args=(xi1__, xi2__), backend='cython', tempdir='./autowraptmp_F')

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
def etta(double xi_1, double xi_2, z0=Matrix([0.1, 0, 0]), dz0=Matrix([0, 0, 0])):
    cdef float T
    cdef Py_ssize_t i
    cdef double[9] coefs
    C1, M1, F1 = Matrix(C_c(xi_1, xi_2)), Matrix(M), Matrix(F_c(xi_1, xi_2))
    P = [sqrt(re(x)) for x in solve((C1 - p * M1).det(), p)]
    for i in range(3):
        p_i = P[i]
        v_i2, v_i3 = symbols('vi2 vi3', real=True)
        v = Matrix([1, v_i2, v_i3])
        eq = (C1 - p_i**2 * M1) * v
        sol = solve([eq[0], eq[1]], v_i2, v_i3)
        V = Matrix([1, sol[v_i2], sol[v_i3]])
        V = V * sqrt(1 / (V.T * M1 * V)[0])
        C_alfa = z0.T * M1 * V
        D_alfa = dz0.T * M1 * V / p_i
        coefs[3*i] = p_i
        coefs[3*i + 1] = float(V[0]*C_alfa[0])
        coefs[3*i + 2] = float(V[0]*D_alfa[0])

    T = 2*3.141592 / coefs[0]

    def etta_(double t):
        cdef Py_ssize_t i
        cdef double value
        value = 0
        for i in range(3):
                value += coefs[3 * i + 1] * cos(coefs[3 * i] * t) + coefs[3 * i + 2] * sin(coefs[3 * i] * t)
        return value
    return etta_, T



@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
def Koshi(double[:, :] A_, double[:, :] B_, double[:, :] D_, double mu, double xi_1, double xi_2, double f0):
    cdef double T
    etta_cur, T = etta(xi_1, xi_2)
    cdef double mu_
    cdef double kappa0
    kappa0 = f0_kappa0[0]
    mu_ = mu
    cdef double[:, :] A
    cdef double[:, :] B
    cdef double[:, :] D
    A = A_
    B = B_
    D = D_
    def Matrix_curr(double t):
        return np.array([
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [-(mu ** 2 - f0 - kappa0 * etta_cur(t)) * D[0][0] / A[0][0], 0, 0, -2 * mu * B[0][1] / A[0][0]],
                [0, -(mu ** 2 - f0 - kappa0 * etta_cur(t)) * D[1][1] / A[1][1], -2 * mu * B[1][0] / A[1][1], 0]
            ], dtype=float)

    return Matrix_curr, T

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
def define_stability(double[:, :] A_, double[:, :] B_, double[:, :] D_, double xi1, double xi2, double[:] f0, double[:] mu):
    cdef Py_ssize_t i, j
    cdef long val
    cdef np.ndarray[np.float64_t, ndim=2] I, Monodromy, StMatr, A, B
    cdef double rho_max, T, h2, Eps_multipliers, t
    cdef int N
    Eps_multipliers = 0.0001
    N = 1000
    I = np.eye(4, 4)
    StMatr = np.zeros((f0.shape[0], mu.shape[0]))
    for i in range(mu.shape[0]):
        for j in range(f0.shape[0]):
            A_matr, T = Koshi(A_, B_, D_, mu[i], xi1, xi2, f0[j])
            h2 = T / N / 2
            A = A_matr(0.0) * h2
            Monodromy = I
            t = 0
            for k in range(N + 1):
                t += h2
                B = A_matr(t) * h2
                Monodromy = (np.linalg.inv(I-B)).dot((I+A).dot(Monodromy))
                A = B
            multipliers = np.linalg.eig(Monodromy)[0]
            rho_max = max(list(map(abs, multipliers)))
            if rho_max > 1 + Eps_multipliers:
                StMatr[j, i] = 1
    return StMatr
