from bs4 import BeautifulSoup 
import requests, re
# 뉴스의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
url = ('https://news.daum.net/')
# 봇으로 인식하지 않기 위해서는 다음과 같은 헤더를 달아줌
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')

# 링크 타고 들어가서 제목과 본문을 같이 크롤링 하는데 성공
for i in soup.find_all('strong', {'class':'tit_thumb'}):
    try:
        print(i.text)
        soup = BeautifulSoup(requests.get(i.find('a').get('href'), headers = headers).text, 'lxml')
        for i in soup.find_all('p'):
            print(i.text)
    except:
        pass
 