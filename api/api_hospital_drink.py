
import requests,re, json
from bs4 import BeautifulSoup

url = "http://apis.data.go.kr/B551172/Lung04/luAlchbyType?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=100&centerNm=%EA%B5%AD%EB%A6%BD%EC%95%94%EC%84%BC%ED%84%B0&fromYear=2010&toYear=2019&type=xml"
# 샘플키는 5개를 넘을 수 없습니다. 
soup = BeautifulSoup(requests.get(url).text, 'lxml')
total = []
total.append([i.text for i in soup.find_all('centernm')])
total.append([i.text for i in soup.find_all('crityr')])
total.append([i.text for i in soup.find_all('ptage')]) 
total.append([i.text for i in soup.find_all('ptsexcd')]) 
total.append([i.text for i in soup.find_all('statstrgtnm')]) 


import pandas as pd 
df = pd.DataFrame(total).transpose()
df.to_clipboard() 

print(df.groupby(df[4]))
 