# 리스트의 생성1
a =[]
print(a)
print(type(a))

# 리스트의 생성2
a =list()
print(a)
print(type(a))

a =[1,2,3,4,5]
print(a)

# 리스트의 요소는 타입이 같을 필요는 없다.
a = ["글자", 123, 123.3]
print(a)

# 리스트의 인덱싱과 슬라이싱
print(a[0]) # 변수명[인덱스값]
print(a[0:2]) # 0번과 1번 출력, 리스트형태로 출력 ["글자", 123]
print(a[:])
print(a[0::2])

# 리스트에 요소 추가
# append() : 제일 마지막 인덱스에 요소를 추가
a =[1,2,3]
a.append(4)
print(a)

# insert() : 인덱스를 지정해서 요소를 추가
a.insert(0,0)
print(a)

# 삭제 : del 인덱스
del a[0]
print(a)

del a[0:2]
print(a)

# 삭제: remove(요소)
a.remove(4)
print(a)

# 삭제 및 값 리턴 pop(인덱스)
a=[0, 1, 2, 3]
print(a.pop(3))  # 인덱스 번호 입력 -> 해당 인덱스 값이 삭제됨
print(a)

# 리스트의 확장 extend()
a = [1,2,3]
b = [4,5,6]
# print(a+b) # 원본은 유지하되 리스트끼리 더함
# print(a)
# print(b) 

a.extend(b) # 원본 리스트 a에 리스트 b를 더한다 
print(a)
print(b) # b의 원본은 유지

a = [4,5,6,3,2,1]

# 오름차순 정렬: sort()
print("** 오름차순 정렬 **")
a.sort()
print(a)

# 내림차순 정렬: reverse()
print("** 내림차순 정렬 **")
a.reverse()
print(a)

print("** 특정 요소 포함 여부: in **")
print(1 in a)
print(10 in a)