from sympy import symbols, Matrix, Symbol, re, sqrt, cos, sin
from sympy.solvers import solve
from sympy.plotting import plot

import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

import os
os.chdir(r'/home/hello/PycharmProjects/NIR_')
from Plate.SubsValues import subs_values

xi_1, xi_2 = 0.5, 0.3
t = Symbol('t')
p = Symbol('p')
xi1__, xi2__ = symbols('xi1__ xi2__', real=True)
M, C, F, b_a, f0_kappa0 = subs_values()
C1, M1, F1 = Matrix(C.subs([(xi1__, xi_1), (xi2__, xi_2)])), Matrix(M), Matrix(F.subs([(xi1__, xi_1), (xi2__, xi_2)]))
P = [sqrt(re(x)) for x in solve((C1 - p * M1).det(), p)]
z0 = Matrix([-0.1, -0.2, -0.3])
dz0 = Matrix([0, 1, 1])
coefs = []

for i in range(3):
    p_i = P[i]
    v_i2, v_i3 = symbols('vi2 vi3', real=True)
    v = Matrix([1, v_i2, v_i3])
    eq = (C1 - p_i**2 * M1) * v
    sol = solve([eq[0], eq[1]], v_i2, v_i3)
    V = Matrix([1, sol[v_i2], sol[v_i3]])
    V = V * sqrt(1 / (V.T * M1 * V)[0])
    C_alfa = z0.T * M1 * V
    D_alfa = dz0.T * M1 * V / p_i
    coefs.append(p_i)
    coefs.append(float(V[0]*C_alfa[0]))
    coefs.append(float(V[0]*D_alfa[0]))


def etta():
    value = 0
    for i in range(3):
            value += coefs[3 * i + 1] * cos(coefs[3 * i] * t) + coefs[3 * i + 2] * sin(coefs[3 * i] * t)
    return value


p1 = plot(etta(), (t, 0, 1), show=True, grid=True, adaptive=False, nb_of_points=10000)

