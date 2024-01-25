# for
# for 변수 in 리스트(튜플, 문자열 -> 인덱스 값을 가지는 객체):
#   수행할 문장
a = ["one", "two", "three"]
for s in a:
    print(s)

# range(start, end, step) : start부터 end -1까지 숫자를 컬렉션으로 만든다.
# start와 step은 생략 가능
for i in range(1,11,2):
    print(i)

# break
n = 0
while True:
    print(n)
    n += 1
    if n == 10:
        break

# continue
n = 0
while n < 10 :
    n += 1
    if n ==5:
        continue # if조건에 만족하면 아래에 있는 문장 출력안함 -> n이 5가 되면 프린트하지않고 다음 진행
    print(n) 

a = "abcdefg"
for s in a:
    print(s)

list = ['one', 'two', 'three']
for i in list:
    print(i)

list = [(1,2), (3,4), (5,6)] #요소가 2개인 튜플이 3개있는 리스트
for i in list:
    print(i)
    for j in i:
        print(j) # 모든 요소 출력 가능

print("< 딕셔너리의 리스트 반복문 출력 - enumerate() 함수 이용 >")
student = [{"홍길동":100}, {"김개똥":200},{"이말똥":300}] #딕셔너리의 리스트
# enumerate() 함수를 이용한 반복
# 순서값과 요소값을 한번에 구해주는 내장함수
# 리스트의 순서값과 요소값을 튜플로 묶은 컬렉션을 리턴
for s, i in enumerate(student, start=1):
    print(s, i)
    # print(s)
    # print(i.items())
#     data = list(i.items())[0]
#     name = data[0]
#     value = data[1]
# print(f"{s} 이름: {name}, 학번: {value}")

print("< Comprehension >")
# Comprehension: 하나 이상의 iterator로부터 파이썬의 자료구조를 만드는 방법
# 1. 리스트 컴프리헨션
#   [표현식 for 항목 in 순회 가능한 객체]

# ex) 1~5 사이의 정수에 5를 더해서 리스트를 생성
result = []
#일반적인 문법
for num in range(1, 6):
    # print(num)
    result.append(num + 5)
# print(result)

#컴프리헨션 문법
result = [num + 5 for num in range(1,6)]
print(result)

# ex) 1~5 사이의 정수 중 짝수인 숫자에 3을 곱해서 리스트를 생성
result = [i*3 for i in range(1,6) if i%2 == 0]
print(result)

# ex) 1~9 사이의 정수를 1~9까지 반복하여 서로 곱한 값을 리스트 생성
result = [i*j for i in range(1,10) for j in range(1,10)]
print(result)

# 구구단 출력
gugudan = [f"{i} * {j} = {i*j}" for i in range(2,10) for j in range(1,10)]
print(gugudan)