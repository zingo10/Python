# {}, set, set() 로 생성
# 순서가 없다. -> 인덱스X
# 중복값을 허용하지 않는다.
# 집합연산 가능 | 합집합 - 차집합 & 교집합

# set의 생성
a = set()
print(a, type(a))

a ={1,2,3}
print(a, type(a))

a =[1,2,3,4,4] # set은 중복을 허용하지 않음
b = set(a) # list를 set함수로 출력 -> 중복된 요소가 제거된 상태로 출력
# print(b)

a = set([1,2,3,4])
b = set([3,4,5,6])
# print(a)
# print(b)

# a와 b의 교집합
# print(a & b)

# a와 b의 합집합
# print(a | b) # 중복값은 제외하고 a,b 두 set이 더해짐

# a와 b의 차집합
# print(a - b)

# 요소 추가 add()
print(a)
a.add(6)
print(a)
a.add(7)
print(a)

# 요소 삭제 remove()
a.remove(7)
print(a)
a.remove(6)
print(a)

# 집합 수정 update()
a.update([5,6,7,8])
print(a)

# 형 변환
a = [1,2,3,4,5,5,5]
b = list(set(a))
print(b)