# get 방식, post 방식(조금 더 안전한 방식)
from bs4 import BeautifulSoup as bs
import requests
import re
new = []
# 책의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
url = ('https://finance.naver.com//item/main.nhn?code=004410')
xpath = '//*[@id="img_chart_area"]'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = bs(res.text, 'lxml')
for i in soup.find_all('div', {'class':'sub_section right'})[1].find_all('li'):
    print(i.find('a').text)
    print(i.find('a').get('href'))
  