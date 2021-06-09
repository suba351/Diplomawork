from sympy import symbols, Matrix, Symbol, re, sqrt
from sympy.solvers import solve
import numpy as np
import os
os.chdir(r'/home/hello/PycharmProjects/NIR_')
from Plate.SubsValues import subs_values
t = Symbol('t')
p = Symbol('p')
xi1__, xi2__ = symbols('xi1__ xi2__', real=True)
M, C, b_a = subs_values()


def etta(xi_1, xi_2, z0=Matrix([1, 0, 0]), dz0=Matrix([0, 0, 0])):
    '''
        Считает нормированный вектор собственных форм (V.T * M * V = 1)
        Вид функции : A_i * cos(p_i*t) + B_i*sin(p_i*t)
        A_i = V[0]*C_alfa[0]
        B_i = V[0]*D_alfa[0]
        Возвращает коэффициенты и частоты в виде функцию этта, которая зависит только от времени
    '''
    coefs = []
    C1, M1 = C.subs([(xi1__, xi_1), (xi2__, xi_2)]), M.subs([(xi1__, xi_1), (xi2__, xi_2)])
    P = [sqrt(re(x)) for x in solve((C1 - p * M1).det(), p)]
    for p_i in P:
        v_i2, v_i3 = symbols('vi2 vi3', real=True)
        v = Matrix([1, v_i2, v_i3])
        eq = (C1 - p_i**2 * M1) * v
        sol = solve([eq[0], eq[1]], v_i2, v_i3)
        V = Matrix([1, sol[v_i2], sol[v_i3]])
        k = sqrt(1 / (V.T * M * V)[0])
        V = k * V
        C_alfa = z0.T * M * V
        D_alfa = dz0.T * M * V / p_i
        coefs.append([float(x) for x in (p_i, V[0]*C_alfa[0], V[0]*D_alfa[0])])
    T = 2*np.pi / coefs[0][0]
    return coefs, T


# разбиваем пластину сеткой (точки контакта)
mesh1 = np.linspace(0.0, 1.0, 41)
mesh2 = np.linspace(0., b_a, 41)
