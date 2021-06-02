import cython
import numpy as np
from sympy.utilities.autowrap import autowrap
from sympy import symbols, Matrix
from Plate.SubsValues import subs_values
t = symbols('t')
xi1__, xi2__ = symbols('xi1__ xi2__', real=True)
M, C, F, b_a = subs_values()

M, C, F, b_a = subs_values()
hi = Matrix([[xi2__, xi2__], [xi2__, xi1__]])
hi_c = autowrap(hi, args=(xi1__, xi2__), backend='cython', tempdir='./autowraptmp')
M_c = autowrap(C, backend='cython', tempdir='./autowraptmp')
F_c = autowrap(F, backend='cython', tempdir='./autowraptmp')

mu = 1
f0 = 1

Matrix = Matrix([
            [0, 0, t, 0],
            [0, 0, 0, 1],
            [-(mu ** 2 - f0), 0, 0, 2],
            [0, 1, 3, 0]
        ])

matrix_c = autowrap(Matrix, backend='cython', tempdir='./autowraptmp')

print(matrix_c(0.1))
print(hi_c(0.1, 10))
print(M_c(0.1, 0.2))
print(F_c(0.1, 0.2))

