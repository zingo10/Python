# 예외처리 try / except

# 방법1
# try:
#   오류 발생 코드...
# except
#   오류 처리 코드...

print("< 모든 에러 처리 >")
try:
    a = [1,2,3,4,5]
    a[5] # IndexError
except: 
    print("오류 발생")

# 방법2
# try:
#   오류 발생 코드...
# except 발생 오류:
#   오류 처리 코드...
    
print("< 특정 에러 처리 >")
try:
    result = 10 /0 
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
except IndexError:
    print("인덱싱 에러")

# 방법3
# try:
#   오류 발생 코드...
# except 발생 오류 as 오류 메세지 변수:
#   오류 처리 코드...
    
print("< 에러 메세지 출력 >")
try:
    print(10 /0)
    a = [1,2,3]
    a[3] 
except (ZeroDivisionError, IndexError) as e:
    print(e)

# 방법4
# try:
#   오류 발생 코드...
# except 발생 오류 as 오류 메세지 변수:
#   오류 처리 코드...
# else:
#   오류가 발생하지 않았을 때 코드...

print("< 오류가 발생하지 않았을 때 >")
try:
    n = 2
    result = 10 / n
except:
    print("나누기 오류 발생")
else:
    print(result)

# 방법5
# try:
#   오류 발생 코드...
# except 발생 오류 as 오류 메세지 변수:
#   오류 처리 코드...
# finally:
#   오류 발생과 관계없이 반드시 실행할 코드...

print("< 오류 발생과 관계없이 반드시 실행 >")
try:
    f = open("sample2.txt", "r") # or mode="r"
    f.write("Hello")
except:
    print("파일 오픈 에러 발생")
finally:
    f.close()
    
