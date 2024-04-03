'''
작성일 : 2024년 3월 27일
작성자 : 컴퓨터공학부 202395007 김수종
설명 : matplotlib 라이브러리 활용
'''

# 맷플롯립 라이브러리 생성
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([78.8, 78.4, 78.7, 78.5, 78.4, 79.2, 78.6]) # 체중 데이터

plt.plot(x, y, color="r", marker="o")
plt.grid() 
plt.show()
