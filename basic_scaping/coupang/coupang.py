# get 방식, post 방식(조금 더 안전한 방식)
from bs4 import BeautifulSoup as bs
import requests
import re
new = []
# 책의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
for page in range(10):
    url = ('https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page='+str(page)+'&rocketAll=false&searchIndexingToken=1=4&backgroundColor=')
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(url, headers = headers)
    soup = bs(res.text, 'lxml')
    for i in soup.find_all('li', {'class':'search-product'}):
        name = i.find('div', {'class':'name'}).text
        #print('https://www.coupang.com'+i.find('a').get('href') )
        try:
            new.append([ name , i.find('strong', {'class':'price-value'}).text,i.find('span', {'class':'rating-total-count'}).text,'https://www.coupang.com'+i.find('a').get('href')])
        except: pass

import usecsv 
new = usecsv.switch(new)
usecsv.writecsv('coupang(p)_suc.csv',new)
# 상품정보 담는 데까지 성공
