import numpy as np
cimport numpy as np

cdef extern from 'wrapped_code_0.h':
    void autofunc(double xi1__, double xi2__, double *out_7829438388371073622)

def autofunc_c(double xi1__, double xi2__):

    cdef np.ndarray[np.double_t, ndim=2] out_7829438388371073622 = np.empty((3,3))
    autofunc(xi1__, xi2__, <double*> out_7829438388371073622.data)
    return out_7829438388371073622