# get 방식, post 방식(조금 더 안전한 방식)
from bs4 import BeautifulSoup  
import requests 
url = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79'
# 문고의 베스트셀러 웹페이지를 가져옵니다.
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')
urls = []
for i in soup.find_all('div',{'class':'title'}):
    try:
        #책의 제목
        print(i.find('a').text)
        # url 
        url2 = i.find('a').get('href')
        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
        res = requests.get(url2, headers = headers)
        soup = BeautifulSoup(res.text, 'lxml')
        print(soup.find('div',{'class':'box_detail_article'}))
    except:
        print('오류가 발견되었습니다')

