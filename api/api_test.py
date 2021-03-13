import requests 
from bs4 import BeautifulSoup
url = 'http://openapi.seoul.go.kr:8088/7150435057736b79373067744f4152/xml/CardSubwayStatsNew/1/50/20210101'
soup = BeautifulSoup(requests.get(url).text, 'lxml')
total = []
total.append([i.text for i in soup.find_all('sub_sta_nm')])
total.append([i.text for i in soup.find_all('ride_pasgr_num')])
total.append([i.text for i in soup.find_all('alight_pasgr_num')])

import pandas as pd 
df = pd.DataFrame(total).transpose()
df.to_clipboard()