#기본: 네이버 웹툰 순위 예쁘게 크롤링하기 
from bs4 import BeautifulSoup as bs
import requests,re
url = ('https://comic.naver.com/webtoon/weekday.nhn')
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = bs(res.text, 'lxml')

# ol만 찾아서 text를 찾을 경우, 성공 그러나 지저분함
for i in soup.find_all('ol', {'id':'realTimeRankUpdate'}):
    print(i.text)

# 10대 실시간 인기만화(남자) 타이틀만 빼기 성공
for i in soup.find_all('div', {'class':'thumb6'}):
    print(i.find('a').get('title'))

# 인기 만화 리스트로 반환하기 성공
for i in soup.find_all('ol', {'id':'realTimeRankFavorite'}):
    print([j.get('title') for j in i.find_all('a')])

