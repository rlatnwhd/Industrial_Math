import numpy as np

a = np.array([[-1, 1],
              [-1, 2],
              [2, 3]])

b = np.array([[-1, 1, -1],
              [2, -3, 2]])

print(np.dot(a, b))