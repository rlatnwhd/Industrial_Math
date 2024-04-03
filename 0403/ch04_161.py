'''
작성일 : 2024년 4월 3일
작성자 : 컴퓨터공학부 202395007 김수종
설명 : sympy 예제 2
'''

from sympy import *

x,y,z=symbols('x y z')

print(solveset(x**2 - 2*x + 1))

# 방정식을 나타내는 Eq 클래스가 있음
# Eq클래스의 인수는 방정식의 좌변과 우변을 제공
# Eq(좌변, 우변)
expr = Eq(x**2, 1)
print(solveset(expr)) # = solveset(Eq(x**2, 1))

# 연립방정식은 linsolve(), nonlinsolve() 함수를 사용
# 방정식이 선형인 경우, linsolve()
# 방정식이 비선형인 경우, nonlinsolve()
# 이러한 인수는 방정식과 변수를 정리한 목록 출력
eq1 = x + y - 7
eq2 = -3 * x - y + 5
print(linsolve([eq1, eq2], [x, y]))

eq3 = x * y - 1
eq4 = x - 2
print(nonlinsolve([eq3, eq4], [x, y]))

# simplify() 함수는 수식을 간단하게 만들수 있음
# 그냥 보기 쉽게 계산해서 짧게 보여줌
print(simplify(cos(x)**2 + sin(x)**2))

expr = x**2 + 5*x + 3*(x-1) + (x-1)**2
print(simplify(expr))

# expand() 함수는 수식 전개
print(expand((x-1)*(x-2)))

# factor() 함수는 수식 인수분해
print(factor(x**3-8))

# collect 함수는 수식을 특정 변수의 다항식으로 정리
expr = x*y + y - 3 + 2*x**2 - z*x**2 + x**3
print(collect(expr, x))

# cancel() 함수는 분수의 분자와 분모를 약분하여 간단하게 표기
expr = (x**2 + 2*x + 1)/(x**2 + x)
print(cancel(expr))