# 파이썬의 데이터 타입
# 1. 논리형(bool): True, False
# 2. 정수형: 10진수, 2진수(0b, 0B), 8진수(0o, 0O), 16진수(0x, 0X)
# 3. 실수: 소수점이 있는 수
# 4. 복소수: 제곱해서 음수가 되는 수
# 5. 문자열

# 1. 논리형(bool) : True, False
a = True
print(a)
b = False
print(b)
print(type(a)) #변수의 타입을 알려줘
print(type(b))
a=1<2
print(a)
print(type(a))

a = bool(True) #생성자 호출(파라미터로 True를 줌)
a = bool(-1)
a = bool(0) #0이면 false 0이 아니면 True
print(a) 

# 2. 정수형(int)
a = 10
print(a)
print(type(a))
a = int(5)
print(a, type(a))

# 3.실수형(float)
a = 3.14
print(a)
print(type(a))
print(a, type(a))

# 4.복소수(complex)
a = 2+3j
print(a)
print(type(a))

# 5.문자열(str)
a = "Hello"
print(a)
a = 'World'
print(a)
print(type(a))
a = """Hello World
안녕하세요
제이름은 홍길동입니다.""" #문자 여러줄 쓸 때 따옴표를 줄 갯수만큼 
print(a)

# 산술연산자
a = 10
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)  #정수와 실수를 구분하지 않음

print(a // b) # 몫 구하기
print(a % b)  # 나머지 구하기
print(a ** b) # 지수계산
