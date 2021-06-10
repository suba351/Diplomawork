from sympy import symbols
import os

os.chdir(r'/home/hello/PycharmProjects/NIR_')
# Запись физических параметров материалов из файла data.txt


def read_data(name='data.txt'):
    with open(name) as f:
        values = {}
        for line in f:
            line = line.rstrip('\r\n')
            number, variable = line.split('#')
            values[symbols(variable, real=True)] = float(eval(number))
    return values
