import numpy as np
cimport numpy as np
import cython
cimport cython
from libc.math cimport pi, cos, sin


def Print():
    cdef np.ndarray[np.float64_t, ndim=2] A
    cdef np.ndarray[np.float64_t, ndim=2] B
    cdef np.ndarray[np.float64_t, ndim=2] D
    A = np.load(r"F:\NIR_4th_semestr\TEST\A_Matrix.npy", allow_pickle=True)
    B = np.load(r"F:\NIR_4th_semestr\TEST\B_Matrix.npy", allow_pickle=True)
    D = np.load(r"F:\NIR_4th_semestr\TEST\D_Matrix.npy", allow_pickle=True)
    return A, B, D


def print_t(float t):
    print(t)
    return

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.overflowcheck(False)
def etta(double[:, :] coefs):

    def etta_(double t):
        cdef double value
        cdef int i
        value = 0
        for i in range(3):
            value += coefs[i][1]*cos(coefs[i][1]*t) + coefs[i][2]*sin(coefs[i][1]*t)
        return value

    return etta_


def Koshi(double[:, :] A, double[:, :] B_, double[:, :] D_, double[:, :] coefs):
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
    print(D[0][0])
    def Matrix(double t):
        print(D[0][0])
        return np.array([
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [-(mu**2 - f0 - kappa0*etta_cur(t))*D[0][0]/A[0][0], 0, 0, -2*mu*B[0][1]/A[0][0]],
            [0, -(mu**2 - f0 - kappa0*etta_cur(t))*D[1][1]/A[1][1], -2*mu*B[1][0]/A[1][1], 0]
        ], dtype='float')

    return Matrix






def test(double x):
    cdef double t
    t = 1
    def hi(double y):
        return x + y + t

    return hi
