#구글 특정이미지 크롤링
import os, re, datetime, random, csv
import requests, time
from bs4 import BeautifulSoup as bs
basic = 'https://ko.wikipedia.org/'
imgname='블랙핑크'
url = 'https://ko.wikipedia.org/wiki/%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = bs(requests.get(url, headers = headers).text, 'lxml')     

os.chdir(r'C:\Users\ERC\Pictures\Saved Pictures')
k=0
#특정 사이트 접속
for i in soup.find_all('div', {'class':'thumbinner'}):
    new = basic + (i.find('a').get('href'))
    soup2 = bs(requests.get(new).text,'lxml')
    for j in soup2.find_all('div',{'class':'fullImageLink'}):
        with open(imgname+'.png','wb') as f:
            f.write(requests.get(j.find('a').get('href')).content)