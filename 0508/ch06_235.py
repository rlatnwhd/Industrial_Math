import numpy as np
import matplotlib.pyplot as plt

def my_tan(x):
    return np.tan(x)

def my_cos(x):
    return np.cos(x)

x_t1 = np.linspace(-1.5, 1.5)
x_t2 = np.linspace(-np.pi/2, np.pi/2)

y_tan1 = my_tan(x_t1)
y_tan2 = my_cos(x_t2)

plt.plot(x_t1, y_tan1, label = "tan")
plt.plot(x_t2, y_tan2, label = "tan")

plt.legend()

plt.grid()

plt.show()