'''
작성일 : 2024년 3월 27일
작성자 : 컴퓨터공학부 202395007 김수종
설명 : matplotlib 라이브러리 활용2
'''

# 맷플롯립 라이브러리 생성
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 300) # -5부터 5까지 300개의 사이값을 추출한다
y1 = x**2
y2 = (x-2)**2

# 축 레이블
plt.xlabel("X-Axis", size=14)
plt.ylabel("Y-Axis", size=14)

# 그래프 제목
plt.title("Graph Title")

# 그리드 표시
plt.grid()

# 범례 및 선 스타일 지정
plt.plot(x, y1, label="y1 value", color="r")
plt.plot(x, y2, label="y2 value", linestyle=":", color="k")
# linestyle 종류 : '-', '--', '-.', ':', 'None', ' ', ''
#                  'solid'(실선), 'dashed'(하이픈), 'dashdot'(하이픈+점), 'dotted'(점)

# 범례 표시
plt.legend()

# 그래프 표시
plt.show()
