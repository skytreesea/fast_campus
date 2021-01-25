# 뷰티풀수프 상용어구
from bs4 import BeautifulSoup  
import requests 
product = '휴대폰거치대'
url='https://en.dict.naver.com/ko/search?query=example' 
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml') 

print(soup.find_all('a'))