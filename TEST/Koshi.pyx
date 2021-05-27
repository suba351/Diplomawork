import numpy as np
cimport numpy as np
from libc.math cimport pi, cos, sin


def Print():
    cdef np.ndarray[np.float64_t, ndim=2] A
    cdef np.ndarray[np.float64_t, ndim=2] B
    cdef np.ndarray[np.float64_t, ndim=2] D
    A = np.load(r"F:\NIR_4th_semestr\TEST\A_Matrix.npy", allow_pickle=True)
    B = np.load(r"F:\NIR_4th_semestr\TEST\B_Matrix.npy", allow_pickle=True)
    D = np.load(r"F:\NIR_4th_semestr\TEST\D_Matrix.npy", allow_pickle=True)
    return A, B, D


def etta(float xi1, float xi2, np.ndarray[np.float64_t, ndim=2] coefs):
    T = 2*pi/coefs[0][0]

    def Print(float t):
        global coefs
        cdef float value
        cdef int i
        value = 0
        for i in range(2):
            value += coefs[i][1]*cos(coefs[i][1]*t) + coefs[i][2]*sin(coefs[i][1]*t)
        return value

    return Print, T

