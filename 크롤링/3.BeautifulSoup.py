# BeautifulSoup: 웹페이지내의 데이터를 쉽게 추출할 수 있도록 도와주는 라이브러리

import requests
from bs4 import BeautifulSoup # bs4 모듈에서 BeautifulSoup만 가져옴

url = 'https://www.google.com'
response = requests.get(url)
html = response.text
# print(html)
soup = BeautifulSoup(html, 'html.parser')

# print(soup.title) # <title> 태그 전체 내용을 가져옴
# print(soup.title.name) # <title> 태그의 이름을 가져옴
# print(soup.title.string) # <title> 태그의 내용을 가져옴

# print(soup.img) # 첫 번째 img 태그 정보를 가져옴
# print("id: " + soup.img['id']) # img 태그의 속성 정보를 가져옴
# print("width: " + soup.img['width']) 

# find() : HTML의 해당 태그에 대한 첫 번째 정보를 가져온다.
# print(soup.find('a'))
# print(soup.find(id='hplogo')) # id가 hplogo인 태그의 정보를 가져옴

# find_all(): HTML의 해당 태그에 대한 모든 정보를 리스트 형식으로 가져옴
print("<<< find_all >>>")
# print(soup.find_all('a'))
print(len(soup.find_all('a'))) # a태그 갯수
print(soup.find_all('a', limit=2)) # 2개만 가져옴
print(soup.find_all('a')[0]) #0번째 인덱스

#css 속성으로 필터링
print("<<< css 속성으로 필터링 >>>")
# print(soup.find_all('span'))
print(soup.find_all('span', class_='gbi'))
print(soup.find_all('span', attrs={'class': 'gbi'}))

# select_one(), select(): css 선택자를 이용하여 원하는 정보를 가져옴
print("<<< css select_one(), select() >>>")
# print(soup.select_one('a'))
# print(soup.select_one('body a'))
# print(soup.select('a'))
print(soup.select('div > a'))

# get_text(): 검색 결과에서 태그를 제외하고 텍스트만 출력
print("<<< get_text() >>>")
data = soup.find('a')
# print(data)
print(data.get_text())




