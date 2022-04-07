import requests,re 
import matplotlib  
from bs4 import BeautifulSoup
# 폰트 안 깨지게 
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False
import matplotlib.pyplot as plt
year = '2018'
cor_type = '공사'
url = 'https://www.cleaneye.go.kr/user/openXmlMajorMngIdx.do?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=500&ac_year='+ year +'&type=xml&SG_APIM=2ug8Dm9qNBfD32JLZGPN64f3EoTlkpD8kSOHWfXpyrY'

soup = BeautifulSoup(requests.get(url, verify = False).text,'lxml')
total  = []
total.append([re.sub('\\n','',i.text) for i in soup.find_all('AC_YEAR'.lower())]) # 조회연도
total.append([re.sub('\\n','',i.text) for i in soup.find_all('ENT_NAME'.lower())]) # 기업명
total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_AN_YUD'.lower())]) # 안정성유동비율
total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_AN_BUD'.lower())]) # 부채비율
total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_HWA_JAD'.lower())]) # 매출액영업이익율 
total.append([re.sub('\\n','',i.text) for i in soup.find_all('ANA_SU_GYUNGD'.lower())]) # 경상수지비율

import pandas as pd 
df = pd.DataFrame(total).transpose()
df.columns=["조회연도", "기업명", "안정성유동비율", "부채비율",'매출액영업이익율','경상수지비율']

# 특정단어 포함
df = df[df['기업명'].str.contains(cor_type)] # 공사, 상수도, 하수도, 공단, 교통공사 등으로 검색 가능
# for i in df.columns[2:]:
#     df[i]=df[i].astype(float)
df.to_clipboard()
print(df)
# 경상수지비율
# plt.bar(df['기업명'][:6], df['매출액영업이익율'][:6]) 
# plt.bar(df['기업명'][:6], df['부채비율'][:6])
# plt.show()