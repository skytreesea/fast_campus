import requests, re
from bs4 import BeautifulSoup

url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=105&DEAL_YMD=202011'
# 파라미터 조정해서 필요한 자료 구하기 
params ={'serviceKey' : '7JlKxM7fEbOErQRa32MtR3/g/Bxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK+w7YSwijxr0Tklej3cOg==', 'pageNo' : '1', 'numOfRows' : '100', 'LAWD_CD' : '11620', 'DEAL_YMD' : '202203' }

soup = BeautifulSoup(requests.get(url, params=params, verify = False).text,'lxml')
total  = []
for j in soup.find_all('item'):
    t= []
    t.append(params['DEAL_YMD'])
    t.append([re.sub('[가-힣, ]','',i) for i in re.split('\>', j.text)][0])
    t.append([re.sub('[가-힣,]','',i) for i in re.split('\>', j.text)][-8])
    t.append([i for i in re.split('\>', j.text)][-12][:-3])
    total.append(t)

# 강남 11680, 관악 11620
import pandas as pd 
df = pd.DataFrame(total) 
# 숫자로 전환
df[1] = df[1].astype(float)
df[2] = df[2].astype(float)
# 평단가 구하기
df[4] = df[1]/df[2]
#클립보드로 복사하기
df.to_clipboard()
print(df[1].describe())
