import numpy as np
cimport numpy as np

cdef extern from 'wrapped_code_1.h':
    void autofunc(double xi1__, double xi2__, double *out_604791730620997460)

def autofunc_c(double xi1__, double xi2__):

    cdef np.ndarray[np.double_t, ndim=2] out_604791730620997460 = np.empty((3,1))
    autofunc(xi1__, xi2__, <double*> out_604791730620997460.data)
    return out_604791730620997460