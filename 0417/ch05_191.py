import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return 3*x + 2*y

def f2(x, y):
    return 2*x**2 - 3*x*y + 4*y**2

x = np.linspace(-3, 7, 100)
y = np.linspace(-3, 7, 100)
X, Y = np.meshgrid(x, y)
Z = f2(X, Y)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')  # subplot을 추가할 때, projection='3d'를 인자로 전달합니다.
# ax = plt.axes(projection='3d') 이 방법도 있음
ax.plot_surface(X, Y, Z)  # plot_surface 메서드를 올바르게 호출합니다.
ax.view_init(40, -110)
plt.xlabel('x')
plt.ylabel('y')
ax.set_zlabel('z')  # set_zlabel을 호출하여 z축 레이블을 설정합니다.
plt.title("Surface Plot")

plt.show()
