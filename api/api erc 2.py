# 출처 https://www.data.go.kr/data/15058242/openapi.do
import requests,re 
import matplotlib  
import pandas as pd 
import numpy as np
from bs4 import BeautifulSoup
# 폰트 안 깨지게 
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False
import matplotlib.pyplot as plt
years = ['2017','2018','2019','2020']
dfs = []
for year in years:
    url = 'https://www.cleaneye.go.kr/user/openXmlMngResult.do?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=500&ac_year='+year+'&type=xml&SG_APIM=2ug8Dm9qNBfD32JLZGPN64f3EoTlkpD8kSOHWfXpyrY'
    soup = BeautifulSoup(requests.get(url, verify = False).text,'lxml')
    total  = []
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('AC_YEAR'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('ENT_NAME'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('BUS_YI'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('BUS_YO'.lower())])  
    total.append([re.sub('\\n','',i.text) for i in soup.find_all('BUS_PROFIT'.lower())])  
    df = pd.DataFrame(total).transpose()
    df.columns=["조회연도", "기업명", "영업이익률", "영업수익",'영업비용']
    dfs.append(df)

df2 = dfs[0]
t = 1
while t < len(years):
    df2 = pd.merge(df2,dfs[t], how ='outer')
    t += 1
# 특정 조건에 따라서 분류하는 코드 
# conditionlist = [df2['기업명'].str.contains('상수도') ,
#                  df2['기업명'].str.contains('하수도'),
#                  df2['기업명'].str.contains('관광공사'),
#                  df2['기업명'].str.contains('공단') ] 
# choicelist = ['상수도','하수도','관광공사','공단']
# df2['소분류'] = np.select(conditionlist, choicelist, default='Not Specified')    

df3 = pd.read_csv(r'C:\Users\user\Documents\지방공기업평가원_김창현\연구\파이썬을 활용한 연구개발\basic erc.csv', encoding = 'cp949')
pd.merge(df2, df3).to_clipboard()
# df2.to_clipboard()

# 경상수지비율
# plt.bar(df['기업명'][:6], df['매출액영업이익율'][:6]) 
# plt.bar(df['기업명'][:6], df['부채비율'][:6])
# plt.show()  