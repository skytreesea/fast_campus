# get 방식, post 방식(조금 더 안전한 방식)
from bs4 import BeautifulSoup  
import requests, re, time
import pandas as pd
# 교보문고의 베스트셀러 웹페이지를 가져옵니다.
url = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')
urls = []
for soup2 in soup.find('ul',{'class':'list_type01'}).find_all('li'):
    try:
        #제목
        print(soup2.find('div',{'class':'title'}).find('a').text)
        #하이퍼링크
        print(soup2.find('div',{'class':'title'}).find('a').get('href'))
        urls.append( soup2.find('div',{'class':'title'}).find('a').get('href'))
        #저자
        print(re.search('[0-9a-zA-Z가-힣]+', soup2.find('div',{'class':'author'}).text).group())
        #가격
        print(re.search('[0-9,]+', soup2.find('div',{'class':'price'}).text).group())
        #평점
        print(soup2.find('div',{'class':'review'}).find('img').get('alt'))
        #리뷰수
        print(soup2.find('div',{'class':'review'}).find('a').text)
        #하이퍼링크
    except:
        pass

new = 'http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791160023176'
for new in urls[:2]:
    time.sleep(3) 
    try:
        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
        res = requests.get(new, headers = headers)
        soup = BeautifulSoup(res.text, 'lxml')
        # print(soup.find('div',{'class':'box_detail_article'}))
        print(soup.find('div',{'class':'cover'}).find('a'))
        with open(r'C:\Users\ERC\Pictures\Saved Pictures\\' + new[-5:]+ '.jpg','wb') as f :
            f.write(requests.get(soup.find('div',{'class':'cover'}).find('img').get('src')).content)
    except:
        pass
    