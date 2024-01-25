# 파일 읽고 쓰기
# File open
# 파일 객체 = open(파일명, 열기 모드)

# 파일 열기 모드
# r(읽기모드): 파일을 읽기 전용으로 open할 때 사용, 모드를 생략할 경우 기본 r 모드로 설정
# w(쓰기모드): 파일의 내용을 쓸 때 사용 해당 파일이 이미 존재하면 원래의 내용을 모두 지우고 덮어쓴다.
# a(추가모드)
# t(문자열모드)
# b(바이너리모드)

file = open("sample.txt", mode="w")
# file.write("안녕 파이썬") # 파일 생성
file.close()

rfile = open("sample.txt", mode="r", encoding="utf-8") # 한글 변환

# 전체 내용을 한번에 가져온다
# content = rfile.read()
# print(content)

# 한 줄씩 읽기
for s in rfile:
    print(s)
rfile.close()