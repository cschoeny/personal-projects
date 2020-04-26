import numpy as np

x1 = np.array([1, 1, 1, 1])
x2 = np.array([0, 1, 1, 1])
x3 = np.array([0, 0, 1, 1])
x4 = np.array([0, 0, 0, 1])

A = np.array([x1, x2, x3, x4])

A


np.linalg.matrix_power(A, 5)
