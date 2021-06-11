import numpy as np
cimport numpy as np

cdef extern from 'wrapped_code_1.h':
    void autofunc(double xi1__, double xi2__, double *out_3590026859986813466)

def autofunc_c(double xi1__, double xi2__):

    cdef np.ndarray[np.double_t, ndim=2] out_3590026859986813466 = np.empty((3,1))
    autofunc(xi1__, xi2__, <double*> out_3590026859986813466.data)
    return out_3590026859986813466