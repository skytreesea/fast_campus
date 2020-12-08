# get 방식, post 방식(조금 더 안전한 방식)
from bs4 import BeautifulSoup as bs
import requests, usecsv
import re
new = []
# 책의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
url = ('https://finance.naver.com/')
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = bs(res.text, 'lxml')
new_list =[]
for i in soup.find_all('tbody', {'id':'_topItems1'}):
    for j in i.find_all('tr'):
        new_list.append([j.find('a').text,'https://finance.naver.com/'+j.find('a').get('href'), j.find('span', {'class':'blind'}).text])

usecsv.writecsv('stocktoday.csv', new_list)