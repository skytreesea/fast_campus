from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
# 교보문고의 베스트셀러 웹페이지를 가져옵니다.
html = urlopen('http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf')
html = BeautifulSoup(html, "html.parser")

# 책의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
page = []
for cover in html.find_all('div', {'class':'detail'}):
    link = cover.select('a')[0].get('href')
    page.append(link)

# 메타 정보로부터 필요한 정보를 추출합니다.메타 정보에 없는 저자 정보만 따로 가져왔습니다.   
for urls in page[:3]:
    html = urlopen(urls)
    html = BeautifulSoup(html, "html.parser")
    title = html.find_all('title')[0].text[:-6]
    author = html.find('meta',{'name':'author'}).get('content')
    price = html.find('span',{'class':'sell_price'}).text
    reviews = html.find('ul',{'class':'list_detail_booklog'}).find_all('div',{'class':'content'})
    print(title, author)
    for review in reviews:
        print(re.sub('\n\n','',review.text))
# 12월 4일 리뷰까지 가져오는데 성공
    #image = html.find('div', {'class':'cover'}).get('img')
    #url = html.find('meta', {'property':'rb:itemUrl'}).get('content')
    #originalPrice = html.find('meta', {'property': 'rb:originalPrice'}).get('content')
    #price = html.find('meta', {'property':'rb:price'}).get('content')

    #print(index+1, title, author, image, url, originalPrice, price)