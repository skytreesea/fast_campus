from bs4 import BeautifulSoup  
import requests,re

basic = 'https://www.coupang.com'
# 상품명 바꾸기 
url = 'https://ko.aliexpress.com/af/%25EB%25AC%25B4%25EC%2584%25A0%25EB%25A7%2588%25EC%259A%25B0%25EC%258A%25A4.html?d=y&origin=n&SearchText=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&catId=0&initiative_id=SB_20210124004715' 
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')
# print([i.find('a') for i in soup.find_all('span')])
print(soup.find_all('span'))
# 큰 카테고리 구하기 
 