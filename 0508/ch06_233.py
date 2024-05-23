import numpy as np
import matplotlib.pyplot as plt

def my_sin(x):
    return np.sin(x)

def my_cos(x):
    return np.cos(x)

def my_tan(x):
    return np.tan(x)

x = np.linspace(-np.pi, np.pi)
x_t = np.linspace(-1.5, 1.5)
y_sin = my_sin(x)
y_cos = my_cos(x)
y_tan = my_tan(x_t)

plt.plot(x, y_sin, label = "sin")
plt.plot(x, y_cos, label = "cos")
plt.plot(x_t, y_tan, label = "tan")

plt.legend()

plt.grid()

plt.show()