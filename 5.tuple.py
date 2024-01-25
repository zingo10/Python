# 기본적으로 list와 동일하지만 불변의 값.
# 값의 생성, 수정, 삭제가 불가능.
# 내부구조가 단순, 읽는 속도가 빠르고 안전 
# 리스트는 [], 튜플은 ()

# 튜플 생성1
a = ()
print(a)
print(type(a))

# 튜플 생성2
a = tuple() # 튜플의 생성자를 호출해서 생성하는 방법
print(a)
print(type(a))

a = [1,2,3,4,5] # list
b = (1,2,3,4,5) # tuple
print(type(a),type(b))
print(a[0])
a[0] = 9 # list는 요소값을 바꿀 수 있음
print(a)
# b[0] = 9 # tuple은 요소값을 바꿀 수 없음, 삭제 불가 -> 읽기 전용
print(b[0])

# 변수 하나에 여러개의 값을 넣으면 튜플로 생성된다.
b = 1,2,3,4,5
print(b)

# 하나의 요소만 가진 튜플 
b = 1, 
print(b)

# 패킹 : 튜플로 만드는 작업
a = 1,2,3,44
print(a)

# 언패킹 : 튜플에서 값을 꺼내는 작업
a1, a2, a3, a4 = a
print(a1,a2,a3,a4) # 튜플의 갯수에 맞게 언패킹 할 수 있음

a = 1,2,3
print(a[1]) # 인덱싱 가능
print(a[0:2]) # 슬라이싱 가능
