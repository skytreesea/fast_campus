#다음 사전 예문 크롤링 기본형
import os , re, datetime, random, csv
import requests
import pandas as pd
from bs4 import BeautifulSoup 
# words를 늘리면 단어 뜻과 예문 출력이 가능함
words=['example','greatest','vindictive','patriotic','strategy','abundant','adjacent']
# 아래 주소에 단어만 더하면 단어 뜻과 예문이 든 페이지로 이동

url = 'https://dic.daum.net/search.do?q='  
def bs(url):
    return BeautifulSoup(requests.get(url).text,'lxml')

def vocabulary(word):
    soup = bs(url + word)
    # 특정 사이트 가서 'href'를 알아낸다. 
    for i in soup.find_all('a',{'class':'txt_cleansch'}):
        soup2 = bs('https://dic.daum.net/'+i.get('href'))
    # 단어와 의미를 뽑는 구절
    meaning =  [word] +[ j.text for j in soup2.find_all('span',{'class':'txt_mean'}) ]
    print(meaning) 
    # 예문 3개를 넣습니다. 
    sentence =[]
    for i in soup2.find_all('span',{'class':'txt_ex'}):
        sentence.append(i.text)
    return meaning[:3] + sentence[:6]
# 빈 리스트를 만듭니다. 
total =[]
# csv형 리스트를 만듭니다. 
for word in words:
    total.append(vocabulary(word))
# 판다스를 이용해 클립보드에 붙여넣습니다. 
df = pd.DataFrame(total)
df.to_clipboard()