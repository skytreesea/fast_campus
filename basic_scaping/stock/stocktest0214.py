# get 방식, post 방식(조금 더 안전한 방식)
from bs4 import BeautifulSoup  
import requests, re
import pandas as pd
import re
new = []
codes= ['363260','262840','950210','366330','277810','321820','248070','163730','348030','352700','086710','375500','236810','368770','257990','322190','367460','253610','365550','369370','357550','314130']
items = ['https://finance.naver.com/item/main.nhn?code=' + i for i in codes]
print(items)
url = 'https://finance.naver.com'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')
# 이름 출력
names = [i.text for i in soup.find('tbody',{'id':'_topItems1'}).find_all('a')]
# 이아이디 새 url 생성
new = [url + i.get('href') for i in soup.find('tbody',{'id':'_topItems1'}).find_all('a')]

def getInfo(url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')
    # 첫번째 값은 문자열로 출력되기 때문에 리스트로 묶어줌
    new = [soup.find('div',{'class':'wrap_company'}).find('a').text] 
    new += [soup.find('p',{'class':'no_today'}).find('span',{'class':"blind"}).text] # 블라인드 안에 원하는 숫자가 있다는 것을 알기 위해서 먼저 크롤링해서 내용을 보아야 함 
    # 이런 식으로 리스트와 리스트를 더해서 하나의 표준 리스트를 만들 수 있음
    new = new + [[i.text for i in soup.find('p',{'class':'no_exday'}).find_all('span')][1]]
    new += [i.text for i in soup.find('p',{'class':'no_exday'}).find_all('span',{'class':"blind"})]
    new += [i.text for i in soup.find('table',{'class':'no_info'}).find_all('span',{'class':"blind"})]
    new = [re.sub(',','',i) for i in new]
    # 숫자만 찾아서 숫자로 만드는 방법
    for i in new:
        try: 
            new[new.index(i)] = float(i)
        except:
            pass
    return new

def get_img(name, url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')
    with open(r'C:\Users\ERC\Pictures\Saved Pictures\\'+name+'.jpg','wb') as f :
        f.write(requests.get(soup.find('img',{'id':'img_chart_area'}).get('src')).content)
k = 0 
total = [] 
#url들의 모음에서 각각 추출하기 
for i in items:
    total.append(getInfo(i))
    get_img(codes[k], i)
    k += 1

import pandas as pd
df = pd.DataFrame(total, columns=['이름',	'현재가', 	'상태',	'전일대비',	'전일대비수익률',	'전일',	'고가',	'상한가',	'거래량',	'저가',	'하한가',	'거래대금'])
df.to_clipboard()