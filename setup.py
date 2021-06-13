from distutils.core import setup
from Cython.Build import cythonize
import numpy

# define an extension that will be cythonized and compiled
setup(
    ext_modules=cythonize("Koshi_mu_f0.pyx"),
    include_dirs=[numpy.get_include()]
)