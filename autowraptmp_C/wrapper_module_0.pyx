import numpy as np
cimport numpy as np

cdef extern from 'wrapped_code_0.h':
<<<<<<< HEAD
    void autofunc(double xi1__, double xi2__, double *out_504200313860085166)

def autofunc_c(double xi1__, double xi2__):

    cdef np.ndarray[np.double_t, ndim=2] out_504200313860085166 = np.empty((3,3))
    autofunc(xi1__, xi2__, <double*> out_504200313860085166.data)
    return out_504200313860085166
=======
    void autofunc(double xi1__, double xi2__, double *out_4062658876925937631)

def autofunc_c(double xi1__, double xi2__):

    cdef np.ndarray[np.double_t, ndim=2] out_4062658876925937631 = np.empty((3,3))
    autofunc(xi1__, xi2__, <double*> out_4062658876925937631.data)
    return out_4062658876925937631
>>>>>>> origin/master