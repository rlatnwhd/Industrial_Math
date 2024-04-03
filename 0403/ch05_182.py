import matplotlib.pyplot as plt
import numpy as np
from sympy import *

a = int(input("상수 입력 : "))
x = np.linspace(0, 5) # x는 0부터 5까지 범위를 가짐
y = a * x # y는 변수


plt.plot(x, y, "r^") # "color, linestyle" 순서 바껴도 상관없음
plt.plot(x, y + 3, "b^") # y축으로 3만큼 평행 이동
plt.xlabel("x", size=15)
plt.ylabel("y", size=15)
plt.grid()

plt.show()