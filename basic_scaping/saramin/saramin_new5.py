# 인기글 스크래핑 제목 성공
import requests, re, time, csv
from bs4 import BeautifulSoup  

# 신규 크롤링
url = 'https://www.saramin.co.kr/zf_user/jobs/hot100'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = BeautifulSoup(requests.get(url, headers = headers).text,'lxml') 
saramin = []
for i in soup.find_all('div',{'class':'list-container'}):
    name =  [i.text for i in soup.find_all('a',{'class':'company_name'})]
    tit =  [i.text for i in soup.find_all('a',{'class':'tit'})]
    dt =  [i.text for i in soup.find_all('dl',{'class':'list_date'})]

saramin.append(name)
saramin.append(tit)
saramin.append(dt)

import pandas 
df = pandas.DataFrame(saramin).transpose()
df.to_clipboard()
