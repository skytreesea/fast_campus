
from bs4 import BeautifulSoup as bs
import requests, usecsv
import re
new = []
# 책의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
url = ('https://new.land.naver.com/search?sk=크로바')
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = bs(requests.get(url, headers = headers).text, 'lxml')

print(soup)
#print(soup.find_all('div', {'class':'item_title'}))

#usecsv.writecsv('realestate(p).csv', new_list)