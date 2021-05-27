from sympy import symbols, diff, simplify, nsolve, sin, sinh
from Plate.ReadData import read_data
from Plate.MC_matrix import MC_matrix
from Plate.PlotGraphs import plot_forms

# Вспомогательные переменные
x, t, xi1, xi2, xi1__, xi2__ = symbols('x t xi1 xi2 xi1__ xi2__', real=True)
alpha_, lambda_ = symbols('alpha_ lambda_', real=True)

values = read_data()
b_a = float(values[symbols('b', real=True)] / values[symbols('a', real=True)])

# функции Крылова
K4 = 1 / 2 * (sinh(x) - sin(x))
K3 = diff(K4, x)
K2 = diff(K3, x)
K1 = diff(K2, x)

# Определение собственных значений для случая заделка / свободный край
# С1 = С2 = 0
Eq1 = simplify(K1 ** 2 - K4 * K2)

alfa1 = nsolve(Eq1, x, 1.2)
alfa2 = nsolve(Eq1, x, 4.5)

# Определение собственных значений для случая свободный край / свободный край
# C3 = C4 = 0
Eq2 = simplify(K3 ** 2 - K2 * K4)

lambda1 = nsolve(Eq2, x, 5) / b_a
lambda2 = nsolve(Eq2, x, 8) / b_a

# Уравнение функций форм в общем виде
fi = K3.subs(x, xi1 * alpha_) - K1.subs(x, alpha_) / K2.subs(x, alpha_) * K4.subs(x, xi1 * alpha_)
psi = K1.subs(x, xi2 * lambda_) - K3.subs(x, lambda_ * b_a) / K4.subs(x, lambda_ * b_a) * K2.subs(x, xi2 * lambda_)

# Выражения функций форм для полученных собственных значений
fi1 = fi.subs(alpha_, alfa1)
fi2 = fi.subs(alpha_, alfa2)
psi1 = psi.subs(lambda_, lambda1)
psi2 = psi.subs(lambda_, lambda2)

# построение детерминантов и форм
plot_forms(b_a, Eq1, Eq2, fi1, fi2, psi1, psi2)

# определение коэффициентов жесткости
MC_matrix(b_a, fi1, psi1, fi2, psi2)
