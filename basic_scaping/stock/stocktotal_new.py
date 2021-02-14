# 좀 더 쉬운 방법으로 모든 종목 크롤링하기 

from bs4 import BeautifulSoup
import requests, re
basic = 'https://www.saramin.co.kr' 
# 특정 종목 주소 
url = 'https://finance.naver.com/sise/entryJongmok.nhn?&page='
def makesoup(url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup
info =[]
for i in range(1,21):
    url = 'https://finance.naver.com/sise/entryJongmok.nhn?&page=' + str(i)
    soup = makesoup(url)
    info += ([[re.sub(r'[\n\t,]','',j.text) for j in i.find_all('td')] for i in soup.find_all('tr')][2:-3])

 
import pandas as pd
df = pd.DataFrame(info,columns=['종목별',	'현재가',	'전일비',	'등락률',	'거래량',	'거래대금(백만)',	'시가총액(억)'])
df.to_clipboard() 