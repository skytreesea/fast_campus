import requests, re
from bs4 import BeautifulSoup

url = 'https://apis.data.go.kr/1613000/ConAdminInfoSvc1/GongsiReg?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=10&sDate=20150101&eDate=20160101&_type=xml&ncrAreaName=%EC%84%9C%EC%9A%B8&ncrAreaDetailName=%EC%A2%85%EB%A1%9C%EA%B5%AC'


soup = BeautifulSoup(requests.get(url,  verify = False).text,'lxml')
total  = []
soup.find_all()
total.append([i.text for i in soup.find_all('ncrGsKname'.lower())])
total.append([i.text for i in soup.find_all('ncrGsMaster'.lower())])
total.append([i.text for i in soup.find_all('ncrGsNumber'.lower())])
total.append([i.text for i in soup.find_all('ncrItemName'.lower())])
total.append([i.text for i in soup.find_all('ncrOffTel'.lower())])


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
# df.to_clipboard()
# print(df[1].describe())