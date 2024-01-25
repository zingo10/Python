# 클래스 (변수 & 함수 둘 다 가짐)

# 클래스의 선언
# class 클래스명:
#   변수 및 함수를 지정

class 클래스명():
    pass # 아무것도 지정안함 -> 빈 클래스
test = 클래스명()
print(type(test))

# 클래스의 생성자
# 두 개 이상의 생성자를 가질 수 없다.
# 생성자의 작성 방법
# __init__
# self: 클래스 내부에서 __init__() 함수의 첫 매개변수로 지정,
#       객체명을 받는 용도로 사용하며 생략이 불가능
# def __init__(self): self 기본 생성자의 형태(함수, 기본생성자는 필수X)
# def __init__(self, a, b): 전달인자 2개를 받는 생성자

class Person:
    def __init__(self, name, age): 
            print("Person 생성")
            self.name = name # person class의 name이라는 변수를 선언, 전역변수
            self.age = age

    def show(self):
          print(f"이름: {self.name}, 나이: {self.age}")
    
    #print(p)가 실행될 때 호출되는 함수 : 문자열값의 포맷을 지정
    def __str__(self):
          return f"Person - name: {self.name}, age: {self.age}"
    
    #프로그램이 종료될 때 자동으로 호출
    def __del__(self):
          print("삭제되었습니다.")

    #크기 비교 함수
    def __lt__(self, other): # lt : 작다
        return self.age < other.age
    def __le__(self, other): # le : 작거나 같다
        return self.age <= other.age
    def __gt__(self, other): # gt : 크다
        return self.age > other.age
    def __ge__(self, other): # ge : 크거나 같다
        return self.age >= other.age
    def __eq__(self, other): # eq : 같다
        return self.age == other.age
    def __ne__(self, other): # lt : 같지 않다
        return self.age != other.age

p1 = Person("홍길동", 25)
print(type(p1))
print(p1)
print(p1.name, p1.age)
p1.show()

p2 = Person("김개똥", 30)
print(p2)

print("< p1과 p2의 나이 비교 >")
print(p1.age < p2.age)
print(p1 < p2)

# 클래스 상속
class Student(Person):
     def __init__(self, std_no, name, age):
          super().__init__(name, age) # 부모의 생성자 호출
          self._std_no = std_no # Student의 필드에는 std_no(학번) 입력
          self._name = name
          self._age = age
     def __str__(self):
          return f"Student - atd_no: {self._std_no}, name: {self._name}, age: {self._age}"

s = Student(100 ,'홍길동', 30)
print(s)