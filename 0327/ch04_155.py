'''
작성일 : 2024년 3월 27일
작성자 : 컴퓨터공학부 202395007 김수종
설명 : sympy 예제
'''

from sympy import *

x = symbols('x')
sqrt(x**2)
print(x)

y = symbols('y', negative=True)
sqrt(y**2)
print(y)

print(Float(0.2, 5)) # 반올림 오류
print(Float('0.2', '5'))

print(Float ('2', 10) + Float( '0.2', 3))

print(Rational(2, 6))

y=symbols('y')
print((x + x * y).subs(x, y))

z = symbols('z')
print((x + y).subs({x: z**2, y: sqrt(2)}))

eq = pi / 2
print(eq)
print(eq.evalf())
print(eq.evalf(6)) # print(N(eq))도 가능, (기본값 15자리)
print(Float(eq.evalf(), '6'))