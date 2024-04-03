'''
작성일 : 2024년 3월 27일
작성자 : 컴퓨터공학부 202395007 김수종
설명 : matplotlib histogram 예제
'''

import matplotlib.pyplot as plt
import numpy as np

data = np.array([60, 71, 62, 62, 62, 62, 62, 71, 65, 68,\
                  65, 66, 66, 67, 67, 68, 68, 68, 69, 60, 71])

plt.hist(data, bins=20) # bins는 구간의 수(기본 값은 10)
plt.show()