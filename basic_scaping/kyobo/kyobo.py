import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
# 교보문고의 베스트셀러 웹페이지를 가져옵니다.
url = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf'
def bs(url):
    return BeautifulSoup(requests.get(url).text,'lxml')
# 책의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
page = []
html = bs(url)
for cover in html.find_all('div', {'class':'detail'}):
    link = cover.select('a')[0].get('href')
    page.append(link)
total = []
# 메타 정보로부터 필요한 정보를 추출합니다.메타 정보에 없는 저자 정보만 따로 가져왔습니다.   
for urls in page[:4]:
    html = bs(urls)
    title = html.find_all('title')[0].text[:-6]
    author = html.find('meta',{'name':'author'}).get('content')
    price = html.find('span',{'class':'sell_price'}).text
    reviews = html.find('ul',{'class':'list_detail_booklog'}).find_all('div',{'class':'content'})
    for review in reviews:
        print([title, author])
        try:
            print(review.text.replace('\n',''))
        except:
            pass