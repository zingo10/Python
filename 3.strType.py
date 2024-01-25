a = "Hello Python"
print(a, type(a))

# 이스케이프 문자
# \n 줄바꿈 문자
print("*****\nHello\nPython\n*****")
# \t 탭
print("hello\tpython")
# \\ 역슬래쉬
print("\\hello python\\")
# \" or \' 따옴표
print("\'hello python\'")

a = "hello"
b = " python"
c = 10
#print(a + b + c)
# print(a + c)   문자열 + 정수 -> 연산불가 (typeerror)
print("*" * 50)

# 문자열 인덱싱 (공백포함)
a = "test python string"
print(a)
print(a[0])
print(a[5])
print(a[-1]) # 음수는 뒤에서부터
print(a[-3])

#[포메팅]
# - 포메팅 : 문자열내에 {} 입력하고 format함수의 인수로 삽입할 변수 또는 값을 입력하면
#       {} 자리에 차례로 인수 값이 전달된다.

name = "홍길동"
age = 25
a = "제 이름은 {}이고 나이는 {}살 입니다.".format(name, age)
print(a)

# - 문자열 포메팅 방식
# %s : 문자열
# %c : 문자 1개 
# %d : 정수
# %f : 실수
# %o : 8진수
# %x : 16진수
# %% : %문자 자체를 출력

a = "제 이름은 %s입니다."%name 
print(a)

a = "제 이름은 %s이고 나이는 %d살입니다"%(name,age)
print(a)

a = "숫자 {}, {}, {}".format(1,2,3)
print(a)
# {} 안에 0부터 시작하는 순서값(인덱스)을 지정할 수 있다.
a = "숫자 {2}, {0}, {1}".format(1,2,3)
print(a)

print(f"제 이름은 {name}이고 나이는 {age}살 입니다.") # 추천!

str1 = "%10s" % "hi" # s -> 자릿수 10자리 확보 후 hi 출력
print(str1)

number = "%2f" % 3.141592 # 소수점 두 자리만 출력
print(number)

# 문자열 관련 함수
test = "abcd 가나다라마바사"
print(test)
# find(), index()는 인덱스값을 리턴
print(test.find("가")) # "가" 문자가 갖는 인덱스값
print(test.find("하")) # 없는 문자을 입력하면 -1값이 리턴됨
# index()는 없으면 오류 발생
# print(test.index("하"))  실행불가
print(test.index("라"))

path = "c:\\test\\abcd\\abcde.jpg" # \를 출력하고 싶으면 \\ 두개 넣기 !
print(path)

print(path.rfind("\\"))
# 경로를 제외한 파일명 찾기
print(path[path.rfind("\\")+1:])

# split : 토큰을 기준으로 나누어 리스트 형태[]로 변환
print(path.split("\\"))

# replace : 문자열 치환
a = "Hello world"
print(a.replace("Hello","Bye"))

# strip : 공백 제거 Ex)로그인시 공백입력실수 방지
a = " test "
print(a.strip())

a = "abcd"
print(a.upper()) # 소문자 -> 대문자
a ="AbCd"
print(a.lower()) # 대문자 -> 소문자

a = "1aaaaaabbbbbbbbbbcccdddddd"
print(a.count("a")) # a가 포함된 문자열의 갯수 반환
print(a.count("bb"))
print(len(a)) # 문자열 전체 길이
print(a.isalpha()) # 알파벳이면 True, 섞여 있으면 False

a = "1234"
print(a.isdecimal()) # 10진수인지 판단하는 함수
print(a.isdigit()) # 아라비아 숫자인지 판단
print(a.isnumeric()) # 수 자체인지 판단

#print(dir(str)) #str 클래스의 함수 목록
#print(dir(int))



