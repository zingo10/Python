# 데코레이터
# 이미 작성된 코드에 새로운 기능을 추가하여 함수의 기능을 확장시키는 개념

def outer_function(mag):
    def inner_function():
        return "inner_function: {}".format(msg)
    return inner_function

result = outer_function("Hello")
print(result)
# print(dir(result))
# print(type(result.__closure__)) # 외부에 
# print(len(result.__closure__))
# print(dir(result.__closure__[0]))
# print(result.__closure__[0].cell_contents)

# 데코레이터 함수
# 함수를 인자로 받아서 새로운 함수를 반환
# @를 이용해서 함수를 데코레이트 할 수 있음

import time # 시간계산과 관련한 모듈
def time_checker(func):
    def inner_func(*args, **kwargs): # 어떤 타입의 파라미터가 들어와도 받을 수 있음
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"함수 {func.__name__} 동작시간: {end_time - start_time}")
        return result
    return inner_func

@time_checker # 함수 데코레이트 하기
def test1():
    for i in range(5):
        time.sleep(0.1)

test1()

@time_checker
def test2():
    for i in range(3):
        time.sleep(0.1)

test2()