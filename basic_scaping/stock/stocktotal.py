# get 방식, post 방식(조금 더 안전한 방식)
from bs4 import BeautifulSoup  
import requests, time
import pandas as pd
import re
new = []

url = ('https://finance.naver.com/')
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')
new_list =[]

def stockInfo(url):
    soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')
    k = 0 
    a = []
    # 상승/하락
    a.append(soup.find('p',{'class':'no_exday'}).find_all('span')[1].text)
    #전일대비 퍼센트 얻어내기(class blind)
    for j in soup.find('p',{'class':'no_exday'}).find_all('span',{'class':'blind'}):
        a.append(j.text)
    #전일, 고가, 저가, 상한가, 거래량 등 
    for i in soup.find('table',{'class':'no_info'}).find_all('span',{'class':"blind"}):
        a.append(i.text)
    return a 

def get_img(name, url):
    soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')
    with open(r'C:\Users\ERC\Pictures\Saved Pictures\\'+name+'.jpg','wb') as f :
        f.write(requests.get(soup.find('img',{'id':'img_chart_area'}).get('src')).content)

# 거래상위, 상한가, 하한가, 시가총액 순위 모아서 보기 
for k in range(1,5):
    for i in soup.find_all('tbody', {'id':'_topItems'+str(k)}):
        for j in i.find_all('tr'):
            try:
                item_url = 'https://finance.naver.com/'+j.find('a').get('href')
                name = j.find('a').text
                print(name)
                new_list.append([name,item_url, j.find('span', {'class':'blind'}).text]+stockInfo(item_url))
                get_img(name, item_url)
            except:
                pass

df = pd.DataFrame(new_list,columns=['종목',	'url' ,	'상승/하락'	,'상승/하락',	'전일대비','	퍼센트',	'전일',	'고가',	'상한가',	'거래량',	'시가',	'저가',	'거래대금'])
#클립보드에 복사 
df.to_clipboard()