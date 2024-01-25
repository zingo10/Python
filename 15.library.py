# import
# 모듈은 파이썬 코드를 작성 해놓은 스크립트 파일
# 스크립트 파일에는 클래스, 함수, 변수 등이 정의되어 있다.
# 외부 모듈을 가져와서 사용할 때는 import 명령을 사용한다.

import math
print(math.sqrt(3)) #루트
print(math.pow(2, 3)) #지수

# math 주요함수
# ceil(x): 올림
# floor(x): 내림
# fabs(x): 절대값
# trunc(X): 소수점 이하 버림

import os
print(os.getcwd())
os.system("cls") # 콘솔 clear
# print(os.listdir("c:\\"))

import time
before = time.time()
print(before)
# time.sleep(1) # 프로그램 1초 쉼
after = time.time()
print(after - before)

import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.date())

import calendar # 달력 귀여워
print(calendar.calendar(2024))
print(calendar.month(2024,1))

import random
print(random.random())
print(random.randint(1,5)) #1~5 사이의 랜덤한 int값을 만들어 줌

a = ["가위", "바위", "보"]
print(random.choice(a)) # 리스트 값중에 랜덤한 하나의 값을 출력
random.shuffle(a)