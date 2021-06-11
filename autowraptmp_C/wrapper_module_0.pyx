import numpy as np
cimport numpy as np

cdef extern from 'wrapped_code_0.h':
    void autofunc(double xi1__, double xi2__, double *out_5363963769937454853)

def autofunc_c(double xi1__, double xi2__):

    cdef np.ndarray[np.double_t, ndim=2] out_5363963769937454853 = np.empty((3,3))
    autofunc(xi1__, xi2__, <double*> out_5363963769937454853.data)
    return out_5363963769937454853