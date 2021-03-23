
basic = 'https://dic.daum.net'
import requests
from bs4 import BeautifulSoup
words  = ['find','search','advantage']
total  = []
for word in words:
    url = 'https://dic.daum.net/search.do?q=' + word
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    new = basic + soup.find('div',{'class':'search_cleanword'}).find('a').get('href')
    soup2 = BeautifulSoup(requests.get(new).text, 'lxml')
    a=[word]
    for i in soup2.find_all('span',{'class':'txt_mean'})[:3]:
        a.append(i.text)
    for i in soup2.find_all('span',{'class':'txt_ex'})[:4]:
        a.append(i.text)
    total.append(a)

import pandas as pd
df = pd.DataFrame(total)
df.to_clipboard()