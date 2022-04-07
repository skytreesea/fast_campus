import requests, re
from bs4 import BeautifulSoup

url = 'http://apis.data.go.kr/1613000/ConAdminInfoSvc1/GongsiReg'
params ={'serviceKey' : '7JlKxM7fEbOErQRa32MtR3/g/Bxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK+w7YSwijxr0Tklej3cOg==', 'pageNo' : '1', 'numOfRows' : '100', 'sDate' : '20211201', 'eDate' : '20221202', '_type' : 'xml', 'ncrAreaName' : '서울', 'ncrAreaDetailName' : '관악구' }

soup = BeautifulSoup(requests.get(url, params=params,  verify = False).text,'lxml')
total  = []
soup.find_all()
total.append([i.text for i in soup.find_all('ncrGsKname'.lower())])
total.append([i.text for i in soup.find_all('ncrGsMaster'.lower())])
total.append([i.text for i in soup.find_all('ncrGsNumber'.lower())])
total.append([i.text for i in soup.find_all('ncrItemName'.lower())])
total.append([i.text for i in soup.find_all('ncrOffTel'.lower())])
total.append([i.text for i in soup.find_all('ncrGsSeq'.lower())]) # 공사일련번호

# 강남 11680, 관악 11620
import pandas as pd 
df = pd.DataFrame(total).transpose()
print(df)
# 숫자로 전환
# df[1] = df[1].astype(float)
# df[2] = df[2].astype(float)
# 평단가 구하기
# df[4] = df[1]/df[2]
#클립보드로 복사하기
df.to_clipboard()
# print(df[1].describe())