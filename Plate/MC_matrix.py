from sympy import symbols
import numpy as np
from Plate.CalcCoeff import a_coeff, integrate_coeff


def MC_matrix(b_a, fi1, psi1, fi2, psi2):
    kappa0, kappa1, kappa2, kappa3, kappa4 = symbols('kappa0 kappa1 kappa2 kappa3 kappa4', real=True)
    xi1, xi2, xi1__, xi2__ = symbols('xi1 xi2 xi1__ xi2__', real=True)
    k0 = symbols('k0', real=True)
    # Коэффициенты при обобщённых координатах в выражении потенциальной энергии при сжатии пружины:
    u11_spring = (fi1.subs(xi1, 1) * psi1.subs(xi2, 0.5 * b_a)) ** 2 * kappa3
    u22_spring = (fi2.subs(xi1, 1) * psi2.subs(xi2, 0.5 * b_a)) ** 2 * kappa3
    u12_spring = fi1.subs(xi1, 1) * psi1.subs(xi2, 0.5 * b_a) * fi2.subs(xi1, 1) * psi2.subs(xi2, 0.5 * b_a) * kappa3

    # Коэффициент при обобщённых координатах в выражении потенциальной энергии при деформации пластины:
    A, B, D = a_coeff(fi1, psi1, fi2, psi2, b_a)
    a_11 = A + u11_spring
    a_22 = B + u22_spring
    a_12 = D + u12_spring
    a_21 = a_12

    # Создание матриц коэффициентов
    # M * ddz + C * z = 0
    m11 = integrate_coeff(fi1**2 * psi1**2, b_a)
    m12 = integrate_coeff(fi1 * fi2 * psi1 * psi2, b_a)
    m21 = m12
    m22 = integrate_coeff(fi2**2 * psi2**2, b_a)

    M = np.array([
        [1*xi1/xi1, 0*xi1, 0*xi1],
        [0*xi1, m11, m12],
        [0*xi1, m21, m22]
    ])

    # Значение перемещения пластины в точке касания ролика
    u1 = fi1.subs(xi1, xi1__)*psi1.subs(xi2, xi2__)
    u2 = fi2.subs(xi1, xi1__)*psi2.subs(xi2, xi2__)


    c11 = a_11 + 2 * kappa4 * u1 ** 2
    c12 = a_12 + 2 * kappa4 * u1 * u2
    c21 = a_21 + 2 * kappa4 * u1 * u2
    c22 = a_22 + 2 * kappa4 * u2 ** 2

    C = np.array([
        [kappa1 - kappa2, -kappa2 * u1, -kappa2 * u2],
        [-kappa4 * u1, c11, c12],
        [-kappa4 * u2, c21, c22]
    ])

    F = np.array([-kappa2 + kappa2, kappa4*u1*k0, kappa4*u2*k0])

    np.save('M_Matrix', M)
    np.save('C_Matrix', C)
    np.save('F_vector', F)
