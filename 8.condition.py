# if
a = 5
b = 3
print("if 실행 전")
if a > b:
    print(f"{b}는 {a}보다 작다.")

if a > 5:
    print(a)
    print("a는 5보다 큽니다.")
elif 1 < a < 5: # 1<a and a>5
    print("a는 1보다 크고 5보다 작습니다.")
    #pass
else:
    print("a는 5와 같다.")
print("if 실행 후") # if문 끝나면 들여쓰기 XX

atr1 = "abcdef"
if "a" in atr1:
    print("있음")
else:
    print("없음")

list = ["홍길동", "김개똥", "이말똥"]
if "홍길동" in list:
    print("yes")
else:
    print("no")
