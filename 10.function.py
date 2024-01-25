# 사용자 정의 함수
def 함수명():
    print("함수 호출") 
    return True
a = 함수명()
print(a)

# 위치 인자를 이용한 함수의 호출
print("< 위치 인자를 이용한 함수의 호출 >")
def restaurant(food, drink, dessert):
    return {'food': food, 'drink': drink, 'dessert': dessert}
    # 딕셔너리 타입으로 리턴(key:value)
first = restaurant('스테이크', '와인', '치즈 케익')
print(first)

# 호출 시 매개변수의 이름을 함께 지정해 순서에 상관없이 호출 가능
print("< 호출 시 매개변수의 이름을 함께 지정해 순서에 상관없이 호출 >")
second = restaurant(drink='막걸리', dessert='잔치국수', food='파전')
print(second)

# 기본 파라미터 : 매개변수의 초기값을 지정하는 것
print("< 기본 파라미터 >")
def rest(food='sushi', drink='sake', dessert='icecream'):
    return {'food': food, 'drink': drink, 'dessert': dessert}
print(rest())
print(rest('돈부리'))
print(rest('돈까스', '맥주', '케이크'))

c = 10
print(c)
def add(a,b):
    global c # 전역변수 C , 함수 밖에서도 함수 내에서와 같은 값으로 사용됨
    c = a + b
    return c
result = add(1,3) # 함수호출(return값)
print(result)
print(c) # 전역변수 c

# 매개변수를 튜플의 형태로 전달
print("< 매개변수를 튜플의 형태로 전달 >")
def save_names(*args):
    print(args)

save_names("홍길동")
save_names("홍길동", "김개똥")

# 매개변수를 딕셔너리 형태로 전달    
print("< 매개변수를 딕셔너리의 형태로 전달 >")
def save_names2(**kwargs):
    print(kwargs)

save_names2(name1 = "홍길동", name2 = "김개똥")

def myfunc1(a, b, *args):
    print(a, b, args)
myfunc1(1, 2)
myfunc1(1, 2, 'a', 'b') # 인덱스 번호에 맞게, 나머지는 튜플의 형태로

def myfunc2(a, b, **kwargs):
    print(a, b, kwargs)

myfunc2('a', 'b')
myfunc2(1, 2, name = '홍길동', age = 20)

def myfunc3(a, b, *args, **kwargs):
    print(a, b, args, kwargs)

myfunc3('a', 10, 'Hello', 20, name = '홍길동', age = 20)

def hi():
    print("Hello")
hello = hi
print(type(hello))
hello()

print("< 함수를 매개변수로 받기 >")
def mul(a, b):
    return a*b

def calc(func, a, b):
    print("결과 {}".format(func(a,b)))

calc(mul, 2, 3)
calc(add, 4, 5)


# def func1(a):
#     if a % 2 == 0:
#         return "짝수"
#     else:
#         return "홀수"
    
# n = input("숫자를 입력하세요 : ")
# # print(func1(int(n)))