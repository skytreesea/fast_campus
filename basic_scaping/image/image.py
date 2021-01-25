#네이버 특정이미지 크롤링
import os, re, datetime, random, csv
import requests
from bs4 import BeautifulSoup as bs
imgname='자유의 여신상'
url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='+imgname
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = bs(requests.get(url, headers = headers).text, 'lxml')
os.chdir(r'C:\Users\ERC\Desktop\이미지저장\이미지')
k =0
for i in soup.find_all('img', {'class':'_img'})[:20]:
    with open(imgname+'image'+str(k)+'.jpg', 'wb') as handler:
        handler.write(requests.get(i.get('data-source')).content)
    k += 1