# Import the extension module hello.
import Koshi
import sys
import numpy as np
sys.path.append(r"F:\NIR_4th_semestr\beam")
sys.path.append(r"C:\users\kirik\appdata\local\programs\python\python37\lib\site-packages")
sys.path.append(r"F:\NIR_4th_semestr\Plate")


# print(sys.path)
# import os
# print(os.getcwd())
# print(os.listdir())
# from beam.DefineFunctionEtta import etta



# coeffs, T = etta(0.1, 0.2)
# print(coeffs)
# coeffs = np.array(coeffs)
# Call the print_result method

coeffs = [[119.70647156248701, 0.0010825618631403865, 0.0], [287.50279265854937, 0.02814203176239039, 0.0], [3128.8357316400056, 0.9999999994866093, 0.0]]
coeffs = np.array(coeffs)
p = np.array([1, 2, 3], dtype=np.float64)

A = np.load(r"F:\NIR_4th_semestr\TEST\A_Matrix.npy", allow_pickle=True)

etta = Koshi.etta(0, coeffs)

print(etta)
