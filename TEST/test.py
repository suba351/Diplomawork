# Import the extension module hello.
import Koshi
import numpy as np
import os
print(os.getcwd())
print(os.listdir())
from beam.DefineFunctionEtta import etta


coeffs, T = etta(0.1, 0.2)
print(coeffs)
coeffs = np.array(coeffs)
# Call the print_result method
p = np.array([1, 2, 3], dtype=np.float64)
t = 0.2

A = np.load(r"F:\NIR_4th_semestr\TEST\A_Matrix.npy", allow_pickle=True)

etta, T = Koshi.etta(0.1, 0.2, coeffs)

print(etta(0.1), T)
