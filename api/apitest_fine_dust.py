import requests,re, json
from bs4 import BeautifulSoup
key = '7JlKxM7fEbOErQRa32MtR3'
# PM10은 미세먼지, PM25는 초미세먼지 
url ='http://openapi.airkorea.or.kr/openapi/services/rest/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=1000&year=2020&itemCode=PM10'


# 해당 페이지에서 되는 url을 가져와서 이것 저것 바꿔보는 것이 가장 좋음
soup = BeautifulSoup(requests.get(url).text, 'lxml')
total = []
# 찾을 때는 소문자로 찾아야 함 
total.append([i.text for i in soup.find_all('districtname')])
total.append([i.text for i in soup.find_all('movename')])
total.append([i.text for i in soup.find_all('issueval')])
total.append([i.text for i in soup.find_all('issuegbn')])
total.append([i.text for i in soup.find_all('issuedate')])
total.append([i.text for i in soup.find_all('issuetime')])
total.append([i.text for i in soup.find_all('cleardate')])
total.append([i.text for i in soup.find_all('cleartime')])
total.append([i.text for i in soup.find_all('clearval')])

import pandas as pd 
df = pd.DataFrame(total).transpose()
df.to_clipboard() 

print(df[0].value_counts().sort_values(ascending = False))
print(df[2].groupby(df[0]))
 