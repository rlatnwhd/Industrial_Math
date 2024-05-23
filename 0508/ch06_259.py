import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4)
y1 = np.abs(x**2 - 4)
y2 = x**2 - 4

plt.plot(x, y1, linestyle="--")
plt.scatter(x, y2)

plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()

plt.show()