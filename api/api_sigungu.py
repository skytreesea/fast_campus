import requests,re
from bs4 import BeautifulSoup

url = 'https://apis.data.go.kr/B551982/openApiSidoCd/openXmlSidoCd?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=300&type=xml&ac_year=2022'

soup = BeautifulSoup(requests.get(url, verify = False).text,'lxml')
total  = []
total.append([re.sub('\\n','',i.text) for i in soup.find_all('SIDO_CD'.lower())])
total.append([re.sub('\\n','',i.text) for i in soup.find_all('SIDO_NAME'.lower())])

import pandas as pd 
df = pd.DataFrame(total).transpose()
df.to_clipboard()
print(df)