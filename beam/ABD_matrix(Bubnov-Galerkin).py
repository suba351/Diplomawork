from scipy import integrate
import numpy as np
from numpy import sin, cos, pi
import os

os.chdir(r'F:\NIR_4th_semestr\beam')


def a11(x):
    return sin(pi*x)*sin(pi*x)


def a12(x):
    return sin(pi*x)*sin(2*pi*x)


def a21(x):
    return sin(2*pi*x)*sin(pi*x)


def a22(x):
    return sin(2*pi*x)*sin(2*pi*x)


def b11(x):
    return pi*cos(pi*x)*sin(pi*x)


def b12(x):
    return pi*cos(pi*x)*sin(2*pi*x)


def b21(x):
    return 2*pi*cos(2*pi*x)*sin(pi*x)


def b22(x):
    return 2*pi*cos(2*pi*x)*sin(2*pi*x)


def d11(x):
    return -4*pi**2*sin(pi*x)*sin(pi*x)


def d12(x):
    return -4*pi**2*sin(pi*x)*sin(2*pi*x)


def d21(x):
    return -4*pi**2*sin(2*pi*x)*sin(pi*x)


def d22(x):
    return -4*pi**2*sin(2*pi*x)*sin(2*pi*x)


A = np.array([
        [integrate.quad(a11, 0, 1)[0], integrate.quad(a12, 0, 1)[0]],
        [integrate.quad(a21, 0, 1)[0], integrate.quad(a22, 0, 1)[0]]
    ])


B = np.array([
        [integrate.quad(b11, 0, 1)[0], integrate.quad(b12, 0, 1)[0]],
        [integrate.quad(b21, 0, 1)[0], integrate.quad(b22, 0, 1)[0]]
    ])


D = np.array([
        [integrate.quad(d11, 0, 1)[0], integrate.quad(d12, 0, 1)[0]],
        [integrate.quad(d21, 0, 1)[0], integrate.quad(d22, 0, 1)[0]]
    ])

np.save('A_Matrix', A)
np.save('B_Matrix', B)
np.save('D_Matrix', D)
