a ={}
print(type(a))

a = dict() # 생성자로 생성
print(type(a))

# {key:value} 딕셔너리의 형태
a = {"name":"홍길동", "age":30} # key값은 중복 불가, value값은 중복 가능
print(a)

# 원소 추가, 바꾸기
print("< 원소 추가, 바꾸기 >")
print(a["name"])
a["name"] = "김정은"
a["age"] = 27
print(a)
a["addr"] = "부산시"
print(a)

# 원소 삭제
print("< 원소 삭제 >")
del a["addr"]
print(a)
a.pop("name")
print(a)

# 딕셔너리 합치기 .update()
print("< 딕셔너리 합치기 >")
a = {"name":"홍길동"}
b = {"age":25}
c = {"addr":"대전"}
a.update(b)
print(a)
a.update(c)
print(a)

# 키만 가져오기
print("< 키만 가져오기 >")
print(a.keys()) # list타입 -> 반복이 가능
for key in a.keys():
    print(key)

# 값만 가져오기
print("< 값만 가져오기 >")
print(a.values())
for value in a.values():
    print(value)

# 키와 값을 모두 가져오기
print("< 키와 값을 모두 가져오기 >")
print(a.items()) # 튜플의 리스트 형식으로 값을 가져옴

print(a["name"])
# print(a["name2"]) # 오류 발생
print(a.get("name"))
print(a.get("name2")) # 없는 값이지만 오류 X

# 요소 포함 여부
print("name" in a)
print("name2" in a)