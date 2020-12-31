# get 방식, post 방식(조금 더 안전한 방식)
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
import re
new = []
# 책의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
for page in range(10):
    url = ('https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page='+str(page)+'&rocketAll=false&searchIndexingToken=1=4&backgroundColor=')
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(url, headers = headers)
    soup = bs(res.text, 'lxml')
    for i in soup.find_all('dd', {'class':'descriptions'}):
        print(i.find('div', {'class':'name'}).text)
        try: 
            print(i.find('span', {'class':'rating-total-count'}).text)
        except: 
            print('평점없음')
