# from urllib import response
import requests # 웹페이지에 요청할 수 있는 모듈: requests
from bs4 import BeautifulSoup # 응답값 분석에 필요한 모듈: BeautifulSoup
import datetime # 날짜 가져오기 위한 모듈
import pandas # 엑셀로 출력

# print((end - start).days)

def get_news(start_date, end_date):

    s_date = start_date.strftime('%Y%m%d')
    e_date = end_date.strftime('%Y%m%d')
    day = end_date - start_date # 몇 일 반복

    result = []

    for i in range(day.days):
        date = start_date + datetime.timedelta(days=i)
        reg_date = date.strftime('%Y%m%d')
        
        url = 'https://news.daum.net/newsbox'
        for j in range(1, 6): # 페이지 반복
            page = j
            #파라미터 세팅
            response = requests.get(url=url, params={'regDate': reg_date, 'page': page}) # 딕셔너리 형태
            # print(response.text) 원하는 정보 잘 가져오는지 확인 
            #   -> 개발자 모드로 필요한 태그 확인 -> BeautifulSoup 이용, 원하는 태그의 내용 가져오기(HTML parsing)
            bs = BeautifulSoup(response.text, 'html.parser')

            trs = bs.select('.list_arrange li') # 선택자 클래스가 list_arrange인 것 가져오기
            if len(trs) < 1:
                break

            # print(trs) # 잘 가져오는지 확인
            for tr in trs:
                # print(tr) # li태그 하나씩 출력하기 위한 반복문
                # 제목 : strong태그 밑에 a의 text를 가져와
                # print("<<< 제목 >>>")
                title = tr.select_one('strong > a').text
                # print(title)

                # 링크
                # print("<<< 링크 >>>")
                link = tr.find('a').get('href')
                # print(link)

                # 언론사
                # print("<<< 언론사 >>>")
                info_news = tr.find('span').text
                # print(info_news)

                # 리스트에 담기(제목, 링크, 언론사)
                # print("<<< 리스트에 담기 >>>")
                print([reg_date, page, title, link, info_news])
                result.append([reg_date, page, title, link, info_news])
                print(result)
    return result

end = datetime.datetime(2024, 1, 25)
start = datetime.datetime(2024, 1, 1)
news = get_news(start, end)

column = ['등록일', '페이지', '제목', '링크', '언론사']
dataframe = pandas.DataFrame(news)
# print(dataframe)
# dataframe.to_excel('news.xlsx', sheet_name='다음 뉴스')