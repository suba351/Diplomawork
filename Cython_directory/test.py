# Import the extension module hello.
import Koshi
import numpy as np

# Call the print_result method
p = np.array([1, 2, 3], dtype=np.float64)
t = 0.2
print(Koshi.Matix(p, t))
Koshi.Print()
