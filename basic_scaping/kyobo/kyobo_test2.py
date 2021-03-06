# get 방식, post 방식(조금 더 안전한 방식)
from bs4 import BeautifulSoup  
import requests, re, time
import pandas as pd
#교보문고의 베스트셀러 웹페이지를 가져옵니다.
url = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')
urls = []
#어떤 뿌리에 있는지를 정확하게 확인 
for i in soup.find('ul',{'class':'list_type01'}).find_all('li'):
    try:
        print(i.find('div',{'class':'title'}).find('a').text)
        urls.append(i.find('div',{'class':'title'}).find('a').get('href'))
    except:
        pass
print(urls)
time.sleep(3)

for url in urls[:4]:
    try:
        url2 = 'http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791160022988'
        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
        res = requests.get(url, headers = headers)
        soup = BeautifulSoup(res.text, 'lxml')
        print(soup.find('div',{'class':'box_detail_article'}))
    except:
        pass