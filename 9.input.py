# 사용자 데이터 입력 데이터 받기
# name = input("이름을 입력하세요: ")
# print(name)

num1 = input("숫자를 입력하세요: ")
print("문자열 입력:", num1, type(num1)) # str -> 문자열 
num2 = int(num1) # int로 형변환
print("int로 형변환:", num2, type(num2)) # int -> 숫자 => 연산이 가능해짐


num3 = input("숫자를 입력하세요 : ")
num4 = input("숫자를 입력하세요 : ")
num3 = int(num3)
num4 = int(num4)
print(f"{num3} + {num4} = {num3 + num4}")