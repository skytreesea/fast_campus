# 뷰티풀수프 상용어구
from bs4 import BeautifulSoup  
import requests,re
#네이버 기사 url만 바꾸기: 따옴표 안에 url을 붙여넣으세요.
productName = '노트북'

basic = 'https://www.coupang.com'
url = 'https://www.coupang.com/np/search?component=&q={}&channel=user'.format(productName)

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')
info=[] 
links = [basic + i.find('a').get('href') for i in soup.find_all('li',{'class':'search-product'})]
for i in soup.find_all('li',{'class':'search-product'}):
    try:
        k=[i.find('div',{'class':'name'}).text, basic + i.find('a').get('href')]
        info.append(k)
    except:
        pass 

print(info[:10])
