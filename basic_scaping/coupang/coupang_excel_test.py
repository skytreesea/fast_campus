# 뷰티풀수프 상용어구
from bs4 import BeautifulSoup  
import requests 
url='https://www.coupang.com/np/search?component=&q=무릎담요&channel=user'
#네이버 기사 url만 바꾸기: 따옴표 안에 url을 붙여넣으세요.
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')
# for i in soup.find_all('div',{'class':'name'}):
#     print(i.text)
# for i in soup.find_all('strong',{'class':'price-value'}):
#     print(i.text)

for i in soup.find_all('ul',{'class':'search-product-list'}):
    print(i.find_all('div',{'class':'name'}))