# 문자열 슬라이싱 
# [:] : 처음부터 끝까지
# [start:] : start부터 끝까지
# [:end] : 처음부터 end-1까지
# [start:end] : start부터 end-1까지
# [start:end:step] : step만큼 건너뛰면서 start부터 end-1까지

a = "test python string"

print(a[0:4]) # 0번 ~ 3번까지(0번에서부터 4개를 가져와)
print(a[0:12])
print(a[0:1000]) # 범위를 넘어도 상관없음
print(a[:12]) # 첫 번째 인덱스 생략가능 (0번부터 출력됨)
print(a[5:]) # 마지막 인덱스 생략가능 (마지막까지 출력됨)
print(a[5:12])
print(a[::2]) # 첫 번째 인덱스 출력, 다음은 두 칸 띄어서 출력

# 문자열 관련 함수
test = "abcd 가나다라마바사"
# find(), index()는 인덱스값을 리턴
print(test.find("가")) # "가" 문자가 갖는 인덱스값
print(test.find("하")) # 없는 문자을 입력하면 -1값이 리턴됨
# index()는 없으면 오류 발생
# print(test.index("하"))  실행불가
print(test.index("라"))

# 경로 정보
path = "c:\\test\\abcd\\abcde.jpg" # \를 출력하고 싶으면 \\ 두개 넣기 !
print(path)

# 인덱스 번호 찾기
print(path.rfind("\\")) # 같은게 있으면 마지막 인덱스 출력
# Q.경로를 제외한 파일명 찾기
print(path[path.rfind("\\")+1:])

# split : 토큰을 기준으로 나누어 리스트 형태[]로 변환
print(path.split("\\"))

# replace : 문자열 치환
a = "Hello world"
print(a.replace("Hello","Bye"))

# strip : 공백 제거 Ex)로그인시 공백입력실수 방지
a = "     test       "
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
print(a.islower()) # 소문자이면 True
print(a.isupper()) # 대문자이면 True

a = "1234"
print(a.isdecimal()) # 10진수인지 판단하는 함수
print(a.isdigit()) # 아라비아 숫자인지 판단
print(a.isnumeric()) # 수 자체인지 판단

#print(dir(str)) #str 클래스의 함수 목록
#print(dir(int))
