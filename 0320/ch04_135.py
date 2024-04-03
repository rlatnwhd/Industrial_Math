'''
작성일 : 2024년 3월 20일
작성자 : 컴퓨터공학부 202395007 김수종
설명 : numpy 라이브러리 활용
'''

import numpy as np # 넘파이 라이브러리 사용

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# 파이썬 리스트를 넘파이 1차원 배열로 만든다
b = np.array([0, 1, 2, 3, 4], [5, 6, 7, 8, 9])
# 파이썬 리스트를 넘파이 2차원 배열로 만든다
c = np.array([0, 1, 2], [3, 4, 5], [6, 7, 8, 9])
# 파이썬 리스트를 넘파이 3차원 배열로 만든다

print(a)

print(a + 3) # 배열의 모든 요소에 3 더하기
print()

print(a * 2) # 배열의 모든 요소 2 곱하기
print()

print(2 ** a) # 배열의 모든 요소에 제곱하기
print()

print(a / 2) # 배열 의 모든 요소를 2로 나누기
print()

print(np.zeros(4)) # 0이 4개로 재워진 배열 생성
print()

print(np.ones((2,3))) # 2차원 배열(행, 열) 을 1로 채워 생성
print()

print(np.arange(0,10)) # 0부터 10-1 까지의 범위가 담긴 배열 생성
print()

print(np.linspace(0,10,3)) # 0부터 10-1 까지의 범위가 담긴 배열 생성 후 범위에 해당하는 숫자를 배열로 출력
print()

print((np.shape(a))) # 배열의 형태 출력 (행, 열)
print()

print(len(a)) # 배열 길이 출력


a = np.array([1, 2], [3, 4])
b = np.array([5, 6], [7, 8])

print(a + b) # 배열의 모든 요소에 b배열을 더하기
print()

print(a - b) # 배열의 모든 요소에 b배열로 빼기
print()

print(a * b) # 배열의 모든 요소에 b배열로 곱하기
print()

print(a / b) # 배열 의 모든 요소를 b배열로 나누기
print()