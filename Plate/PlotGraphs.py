import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, lambdify

"""
    построение графиков функции
"""


def plot_graph(func, x_limit=None, variable=symbols('x', real=True),
               graph_name=None, x_axis_name=None, y_axis_name=None, title_name=None):
    if x_limit is None:
        x_limit = [0, 1]
    cm = 1/2.54
    x_left, x_right = x_limit[0], x_limit[1]
    x_space = np.linspace(x_left, x_right, 101)
    y_space = lambdify(variable, func, 'numpy')
    plt.figure(graph_name, figsize=(15*cm, 5*cm))
    plt.grid(True)
    plt.xlabel(x_axis_name, fontsize=12)
    plt.ylabel(y_axis_name, fontsize=12)
    plt.title(title_name, fontsize=12)
    plt.plot(x_space, y_space(x_space), 'g', linewidth=2)
    plt.plot([x_left, x_right], [0, 0], 'r', linewidth=1)
    return ()


def plot_3d(func, x1_lim, x2_lim, graph_name=None, x_axis_name=None, y_axis_name=None):
    xi1, xi2 = symbols('xi1 xi2', real=True)
    x1_space, x2_space = np.mgrid[0:x1_lim:101j, 0:x2_lim:101j]
    x3_space = lambdify((xi1, xi2), func, 'numpy')
    x3_space = x3_space(x1_space, x2_space)
    fig = plt.figure(graph_name)
    ax = fig.add_subplot(111, projection='3d')
    plt.xlabel(x_axis_name, fontsize=12)
    plt.ylabel(y_axis_name, fontsize=12)
    ax.plot_surface(x1_space, x2_space, x3_space, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    return ()


def plot_forms(b_a, Eq1, Eq2, fi1, fi2, psi1, psi2):
    xi1, xi2 = symbols('xi1 xi2', real=True)
    x1_lim = [0, 6]  # Границы по x1
    plot_graph(Eq1, x1_lim, graph_name='Determine 1', x_axis_name=r'$\alpha$',
               title_name='Определитель матрицы для "Балки 1"')  # строим график детерминанта
    plt.xlim(x1_lim[0], x1_lim[1])
    plt.ylim(-9, 6)

    x2_lim = [0, 10]  # Границы по x2
    plot_graph(Eq2, x2_lim, graph_name='Determine 2', x_axis_name=r'$\lambda$',
               title_name='Определитель матрицы для "Балки 2"')  # строим график детерминанта
    plt.xlim(x2_lim[0], x2_lim[1])
    plt.ylim(-210, 110)

    # Построение графики функций форм для "балок"
    plot_graph(fi1, [0, 1], graph_name='fi1', variable=xi1, x_axis_name=r'$\xi_1$',
               y_axis_name=r'$\varphi (\alpha_1 \xi_1)$', title_name='Первая форма для "Балки 1"')
    plot_graph(fi2, [0, 1], graph_name='fi2', variable=xi1, x_axis_name=r'$\xi_1$',
               y_axis_name=r'$\varphi (\alpha_2 \xi_1)$', title_name='Вторая форма для "Балки 1"')
    plot_graph(psi1, [0, b_a], graph_name='psi1', variable=xi2, x_axis_name=r'$\xi_2$',
               y_axis_name=r'$\psi (\lambda_1 \xi_2)$', title_name='Первая форма для "Балки 2"')
    plot_graph(psi2, [0, b_a], graph_name='psi2', variable=xi2, x_axis_name=r'$\xi_2$',
               y_axis_name=r'$\psi (\lambda_2 \xi_2)$', title_name='Вторая форма для "Балки 2"')

    # Строим графики функций форм для пластины
    plot_3d(fi1 * psi1, 1, b_a, graph_name='fi1_psi1')
    plot_3d(fi1 * psi2, 1, b_a, graph_name='fi1_psi2')
    plot_3d(fi2 * psi1, 1, b_a, graph_name='fi2_psi1')
    plot_3d(fi2 * psi2, 1, b_a, graph_name='fi2_psi2')
    plt.show()

