#네이버 메인에 있는 주요 글들 출처와 내용의 일부를 크롤링하기
import os , re, datetime, random, csv
import numpy as np
import requests
from bs4 import BeautifulSoup as bs
# words를 늘리면 단어 뜻과 예문 출력이 가능함
url='https://www.naver.com/'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = bs(requests.get(url, headers = headers).text, 'lxml')
for title in soup.find_all('li', {'class':'theme_item'}):
    print(title.text)
    print(title.find('a').get('href'))
    