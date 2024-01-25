# 웹 크롤링
# 1. 데이터를 수집하고자 하는 페이지에 접속해서 HTML 데이터를 받는다.
# 2. HTML 데이터를 분석해서 추출이 가능한 형태로 가공한다.
# 3. 데이터 추출

import requests
# requests는 HTTP 요청을 보내기 위한 라이브러리
# 웹 서버에 get, post, put, delete 등의 방식으로 요청을 보내고 응답정보를 받음


url = 'http://www.naver.com'
response = requests.get(url) # url의 응답데이터를 response로 받아옴
# print(response, type(response))
# print(dir(response))
print(response.text)

# 네이버 검색 키워드 요청
url = 'https://search.naver.com/search.naver' 
param = {'query': 'iphone'}
reponse = requests.get(url, params=param)
print(response.text)

# 구글 검색 키워드 요청
url = 'https://search.google.com/search'
param = {'q': 'iphone'}
reponse = requests.get(url, params=param)
print(response.text)

print(response.status_code) # 응답 상태 코드
print(response.headers) # 헤더 정보
print(response.cookies) # 쿠키 정보
print(response.json) # dict 타입의 데이터의 경우
