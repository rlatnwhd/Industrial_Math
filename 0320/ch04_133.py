'''
작성일 : 2024년 3월 20일
작성자 : 컴퓨터공학부 202395007 김수종
설명 : 함수를 이용하여 사칙연산을 하는 프로그램 만들기
'''

def add(num1, num2):
    return (num1+num2)

def minus(num1, num2):
    return (num1-num2)

def multi(num1, num2):
    return (num1*num2)

def disvi(num1, num2):
    return (num1/num2)

end = 'y'
while(end == 'y' or end == 'Y'):
    num1 = int(input("첫 번쨰 정수 입력 : "))
    num2 = int(input("두 번쨰 정수 입력 : "))
    oper = input("연산자 입력(+, -, *, /) : ")

    if oper == '+':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif oper == '-':
        print(f"{num1} - {num2} = {minus(num1, num2)}")
    elif oper == '*':
        print(f"{num1} * {num2} = {multi(num1, num2)}")
    elif oper == '/':
        print(f"{num1} / {num2} = {disvi(num1, num2)}")
    else :
        print("잘못된 연산자 입니다.")
    end = input("계속 하시겠습니까?(y/n) : ")

print("프로그램을 종료합니다.")
