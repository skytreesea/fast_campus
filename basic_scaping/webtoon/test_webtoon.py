#기본: 네이버 웹툰 순위 예쁘게 크롤링하기 
from bs4 import BeautifulSoup
import requests,re
url = ('https://comic.naver.com/webtoon/weekday.nhn')
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')  
new=[]
# 엑셀파일 형태로 저장하려면? 
for i in soup.find_all('ol',{'id':'realTimeRankFavorite'}):
    for j in i.find_all('a'):
        k = [j.text, 'https://comic.naver.com'+j.get('href')]
        new.append(k)
        k=[]
        
import pandas as pd 
df = pd.DataFrame(new).to_clipboard()
df = pd.DataFrame(new).to_excel(r'C:\Users\ERC\Documents\GitHub\fast_campus\basic_scaping\webtoona.xls')

 # 10대 실시간 인기만화(남자) 타이틀만 빼기 성공
for i in soup.find_all('div', {'class':'thumb6'}):
    print(i.find('a').get('title'))

