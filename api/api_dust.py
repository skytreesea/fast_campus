import requests 
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=200&year=2020&itemCode=PM25'
soup = BeautifulSoup(requests.get(url).text, 'lxml')
total = []
total.append([i.text for i in soup.find_all('districtname')])
total.append([i.text for i in soup.find_all('movename')])
total.append([i.text for i in soup.find_all('issuedate')])
total.append([i.text for i in soup.find_all('issuetime')])
total.append([i.text for i in soup.find_all('issueval')])
total.append([i.text for i in soup.find_all('issuegbn')])
total.append([i.text for i in soup.find_all('cleardate')])
total.append([i.text for i in soup.find_all('cleartime')])

import pandas as pd 
df = pd.DataFrame(total).transpose()
df.to_clipboard()
print(df[0].value_counts())