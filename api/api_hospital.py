import requests 
from bs4 import BeautifulSoup

url = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=200&spclAdmTyCd=97'

soup = BeautifulSoup(requests.get(url).text,'lxml')
total  = []
total.append([i.text for i in soup.find_all('sggunm')])
total.append([i.text for i in soup.find_all('yadmnm')])
total.append([i.text for i in soup.find_all('telno')])

import pandas as pd 
df = pd.DataFrame(total).transpose()
df.to_clipboard()