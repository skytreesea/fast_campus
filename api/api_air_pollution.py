import requests,re
from bs4 import BeautifulSoup

url = 'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&returnType=xml&numOfRows=1000&pageNo=1&sidoName=%EC%A0%84%EA%B5%AD&ver=1.0'

soup = BeautifulSoup(requests.get(url, verify = False).text,'lxml')
total  = []

total.append([re.sub('\\n','',i.text[:10]) for i in soup.find_all('dataTime'.lower())])
total.append([re.sub('\\n','',i.text) for i in soup.find_all('sidoName'.lower())])
total.append([re.sub('\\n','',i.text) for i in soup.find_all('stationName'.lower())])
total.append([re.sub('\\n','',i.text) for i in soup.find_all('pm10Value'.lower())])
total.append([re.sub('\\n','',i.text) for i in soup.find_all('pm25Value'.lower())])

import pandas as pd 
df = pd.DataFrame(total).transpose()
df.to_clipboard()
print(df)