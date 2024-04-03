'''
작성일 : 2024년 3월 27일
작성자 : 컴퓨터공학부 202395007 김수종
설명 : numpy 3차원 배열
'''

# 넘파이 라이브러리 생성
import numpy as np

a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) # 3차원 배열

print("합계 :", np.sum(a))
print("평균 :", np.average(a))
print("최댓값 :", np.max(a))
print("최솟값 :", np.min(a))
print("배열 크기 :", np.shape(a)) # 면 X 행 X 열
print("배열 차원", np.ndim(a)) # 3차원 배열 확인
print(a.sum(axis=0)) # 면
print(a.sum(axis=1)) # 행
print(a.sum(axis=2)) # 열