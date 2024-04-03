'''
작성일 : 2024년 3월 20일
작성자 : 컴퓨터공학부 202395007 김수종
설명 : 1부터 100까지의 합을 구하기
'''
# for문 활용
num = 0

for i in range(1, 101):
    num += i

print(num)


# while문 활용
num2 = 0
j = 0

while (j < 100):
    j += 1
    num2 += j

print(num2)