import requests,re
from bs4 import BeautifulSoup

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=100&startCreateDt=20210310&endCreateDt=20220406'

soup = BeautifulSoup(requests.get(url, verify = False).text,'lxml')
total  = []
total.append([re.sub('\\n','',i.text)[:10] for i in soup.find_all('createDt'.lower())])
total.append([re.sub('\\n','',i.text) for i in soup.find_all('decideCnt'.lower())])
total.append([re.sub('\\n','',i.text) for i in soup.find_all('deathCnt'.lower())])

import pandas as pd 
df = pd.DataFrame(total).transpose()
df.to_clipboard()
print(df)