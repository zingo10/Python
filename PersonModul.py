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
    
    def add(a,b):
         return a+b