import numpy as np
import matplotlib.pyplot as plt

def myfunc1(x):
    return 5*x**2 - 3*x + 7

def myfunc2(x):
    return 4*x**3 - 2*x**2 + x - 4

def myfunc3(x):
    return 2*x**3 + 3*x**2 - 4*x -1

x = np.linspace(-2,2)
y1 = myfunc1(x)
y2 = myfunc2(x)
y3 = myfunc3(x)

plt.plot(x, y1, label = "6.1")
plt.plot(x, y2, label = "6.2")
plt.plot(x, y3, label = "6.3")

plt.xlabel("x", size = 14)
plt.ylabel("y", size = 14)

plt.legend()

plt.grid()

plt.show()