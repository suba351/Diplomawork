import numpy as np
cimport numpy as np
from libc.math cimport pi, cos
DTYPE = np.float64

cdef np.ndarray[np.float64_t, ndim=2] A
cdef np.ndarray[np.float64_t, ndim=2] B
cdef np.ndarray[np.float64_t, ndim=2] C

A = np.zeros((2,2), dtype=float64)
B = np.zeros((2,2), dtype=float64)
C = np.zeros((2,2), dtype=float64)

# A = np.load(r"F:\NIR_4th_semestr\Cython_directory\A_Matrix", allow_pickle=True)
# B = np.load(r"F:\NIR_4th_semestr\Cython_directory\B_Matrix", allow_pickle=True)
# D = np.load(r"F:\NIR_4th_semestr\Cython_directory\D_Matrix", allow_pickle=True)






def Matix(np.ndarray[dtype=np.float64_t, ndim=1] p, np.float64_t t):
    cdef np.ndarray[dtype=np.float64_t, ndim=2] A
    A = np.zeros((4,4), dtype=DTYPE)
    A[0, 0] = 0
    A[0, 1] = pi
    A[1, 0] = pi * -(p[0] + p[1] * cos(2 * pi * t))
    A[1, 1] = pi * -p[2]
    return (A)


cdef int x = 1


def Print():
    print(x)
    return