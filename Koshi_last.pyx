import cython
cimport cython
import numpy as np
cimport numpy as np
from libc.math cimport pi, cos, sin


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
def etta(double[:,:] coefs):

    @cython.boundscheck(False)
    @cython.wraparound(False)
    @cython.overflowcheck(False)
    def etta_(double t):
        cdef double value
        cdef int i
        value = 0
        for i in range(3):
            value += coefs[i][1] * cos(coefs[i][1] * t) + coefs[i][2] * sin(coefs[i][1] * t)
        return value

    return etta_



@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
def Koshi(double[:, :] A_, double[:, :] B_, double[:, :] D_, double[:, :] coefs):
    etta_cur = etta(coefs)
    cdef double mu
    cdef double kappa0
    cdef double f0
    mu = 1
    kappa0 = 1
    f0 = 1
    cdef double[:, :] A
    cdef double[:, :] B
    cdef double[:, :] D
    A = A_
    B = B_
    D = D_

    @cython.boundscheck(False)
    @cython.wraparound(False)
    @cython.overflowcheck(False)
    def Matrix(double t):
        return np.array([
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [-(mu ** 2 - f0 - kappa0 * etta_cur(t)) * D[0][0] / A[0][0], 0, 0, -2 * mu * B[0][1] / A[0][0]],
            [0, -(mu ** 2 - f0 - kappa0 * etta_cur(t)) * D[1][1] / A[1][1], -2 * mu * B[1][0] / A[1][1], 0]
        ], dtype='double')

    return Matrix

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
def define_stability(double[:, :] A_, double[:, :] B_, double[:, :] D_, double[:, :] coefs, double[:] xi1_args, double[:] xi2_args):

    cdef np.ndarray[np.float64_t, ndim=2] I, Monodromy, StMatr
    cdef np.ndarray[np.float64_t, ndim=1] TT
    cdef double rho_max, T, h2, Eps_multipliers, t, x, y
    cdef int x_iter, y_iter, N
    Eps_multipliers = 0.0001
    N = 1000
    T = 1
    I = np.eye(4, 4)
    StMatr = np.zeros((xi1_args.shape[0], xi2_args.shape[0]))
    for x in xi1_args:
        y_iter = 0
        for y in xi2_args:
            TT = np.linspace(0, T, N + 1)
            h2 = T / N / 2
            A_matr = Koshi(A_, B_, D_, coefs)
            A = A_matr(TT[0]) * h2
            Monodromy = I
            for t in TT[1:]:
                B = A_matr(t) * h2
                Monodromy = (np.linalg.inv(I-B)).dot((I+A).dot(Monodromy))
                A = B
            multipliers = np.linalg.eig(Monodromy)[0]
            rho_max = max(list(map(abs, multipliers)))
            if rho_max > 1 + Eps_multipliers:
                StMatr[x_iter, y_iter] = 1
            y_iter += 1
        x_iter += 1
    return StMatr
