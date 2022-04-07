#-*- coding: utf-8 -*-
import requests,re, json
from bs4 import BeautifulSoup

url = "http://openapi.seoul.go.kr:8088/79574c4763736b793337784672564c/xml/CardSubwayPayFree/1/500/201502/"
# 샘플키는 5개를 넘을 수 없습니다. 
sample = 'http://openapi.seoul.go.kr:8088/sample/xml/CardSubwayPayFree/1/5/201202/'
soup = BeautifulSoup(requests.get(url).text, 'lxml')
total = []
total.append([i.text for i in soup.find_all('use_mon')]) 
total.append([i.text for i in soup.find_all('sub_sta_nm')])
total.append([i.text for i in soup.find_all('PAY_RIDE_NUM'.lower())])
total.append([i.text for i in soup.find_all('free_RIDE_num'.lower())])
total.append([i.text for i in soup.find_all('PAY_alight_NUM'.lower())])
total.append([i.text for i in soup.find_all('free_alight_num')])
print(total)
import pandas as pd 
df = pd.DataFrame(total).transpose()
df.columns=['연월','역명','유료승차','무료승차','유료하차','무료하차']
for i in df.columns[2:]:
    df[i] = df[i].astype(int)
df.to_clipboard()  
df['new'] = df['무료승차']/(df['유료승차'] +df['무료승차'])
print(df['new'].describe())