#-*- coding: utf-8 -*-
import requests,re, json
from bs4 import BeautifulSoup

url = "http://openapi.seoul.go.kr:8088/79574c4763736b793337784672564c/xml/CardSubwayPayFree/1/100/202102/"
# 샘플키는 5개를 넘을 수 없습니다. 
sample = 'http://openapi.seoul.go.kr:8088/sample/xml/CardSubwayPayFree/1/5/202102/'
soup = BeautifulSoup(requests.get(url).text, 'lxml')
total = []
total.append([i.text for i in soup.find_all('use_mon')])
total.append([i.text for i in soup.find_all('sub_sta_nm')])
total.append([i.text for i in soup.find_all('pay_alight_num')])
total.append([i.text for i in soup.find_all('free_alight_num')])
print(total)
import pandas as pd 
df = pd.DataFrame(total).transpose()
df.to_clipboard()  