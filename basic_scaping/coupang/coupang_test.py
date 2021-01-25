from bs4 import BeautifulSoup  
import requests,re

basic = 'https://www.coupang.com'
# 상품명 바꾸기 
url = 'https://www.coupang.com/np/search?component=&q=무릎담요&channel=user' 
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')
total =[]

# 큰 카테고리 구하기 
for i in soup.find_all('li',{'class':'search-product'}):
    try:
        k=[]
        # 이름
        k.append(i.find('div',{'class','name'}).text)
        # 가격
        k.append(i.find('strong',{'class','price-value'}).text)
        # 상품평
        k.append(i.find('span',{'class','star'}).text)
        # 리뷰수: 마이너스 없애기
        k.append(i.find('span',{'class','rating-total-count'}).text[1:-1])
        # 링크
        k.append('https://www.coupang.com/'+i.find('a').get('href'))
        # 이미지 주소
        k.append('https:'+i.find('img').get('src'))
        # 로켓여부 포함
        if i.find('span',{'class','badge rocket'}):
            k.append('로켓')
        else: 
            k.append('n/a')
        total.append(k)
    except:
        pass
# 데이터프레임 저장하기 
import pandas as pd 
df = pd.DataFrame(total, columns = ['이름','가격','상품평','리뷰수','링크','이미지','로켓배송'])
df.to_clipboard()


