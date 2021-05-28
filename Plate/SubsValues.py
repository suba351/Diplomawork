import numpy as np
from Plate.ReadData import read_data
from sympy import symbols, Matrix, sqrt


def subs_values():
    a, b, E, mu, D, k, k_rez, rho, h, p0, b_a, h_r, k0 = symbols('a b E mu D k k_rez rho h p0_2 b_a h0 k0', real=True)
    M_rol, A_len, l_len, E_len, h_r = symbols('M_rol A_len l_len E_len h_r', real=True)
    kappa1, kappa2, kappa3, kappa4 = symbols('kappa1 kappa2 kappa3 kappa4', real=True)
    """
        a - длина пластины
        b - ширина пластины
        E, mu, D - модуль Юнга, коэффициент Пуассона, цилиндрическая жесткость пластины
        k - жесткость пружин Ролика и Пластины (конусная бабка моделируется пружиной)
        k_rez - коэффициент резания = предел текучести материала пластины * ширину ленты
        rho - плотность материала пластины
        h - толщина пластины

        M_rol - масса ролика
        A_len - площадь сечения ленты
        l_len - длина ленты (расстояние от шарнира до ролика)
        E_len - модуль Юнга ленты
        h_r - толшина резания (толщина снимаемого слоя материала)

    """
    # считываем характеристики материалов и прочее из файла data.txt
    values = read_data()

    values[D] = values[E] * values[h] ** 3 / (12 * (1 - values[mu] ** 2))
    values[k0] = values[h_r] / values[a]
    kappa = dict()
    values[p0] = sqrt(values[D] / (values[rho] * values[h] * values[a] ** 4))
    kappa[kappa1] = (values[k] + values[E_len] * values[A_len] / values[l_len]) / (values[M_rol] * values[p0])
    kappa[kappa2] = (values[k_rez]) / (values[M_rol] * values[p0])
    kappa[kappa3] = (values[k] * values[a] ** 2) / (values[D])
    kappa[kappa4] = (values[k_rez] * values[a] ** 2) / (values[D])

    # загружаем матрицы масс и жесткости
    M = Matrix(np.load(r"/home/hello/PycharmProjects/NIR_/M_Matrix.npy", allow_pickle=True))
    C = Matrix(np.load(r"/home/hello/PycharmProjects/NIR_/C_Matrix.npy", allow_pickle=True))
    F = Matrix(np.load(r"/home/hello/PycharmProjects/NIR_/F_vector.npy", allow_pickle=True))
    # подставляем значения параметров в матрицы (кроме координат контакта)
    for x in kappa:
        M = M.subs(x, kappa[x])
        C = C.subs(x, kappa[x])
        F = F.subs(x, kappa[x])

    M = M.subs(mu, values[mu])
    C = C.subs(mu, values[mu])
    F = F.subs(k0, values[k0])
    return M, C, F, float(values[b] / values[a])
