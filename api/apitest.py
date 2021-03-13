import requests,re, json
from bs4 import BeautifulSoup
key = '7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D'

keys = '714b6e6e50736b7935335a4e66547a'
# 해당 페이지에서 되는 url을 가져와서 이것 저것 바꿔보는 것이 가장 좋음
urls = 'http://openapi.seoul.go.kr:8088/714b6e6e50736b7935335a4e66547a/xml/SearchOpenAPIService/1/200/'
soup = BeautifulSoup(requests.get(urls).text, 'lxml')
print(soup)
total = []
# 찾을 때는 소문자로 찾아야 함 
total.append([i.text for i in soup.find_all('inf_nm')])
total.append([i.text for i in soup.find_all('exm_nm')])
total.append([i.text for i in soup.find_all('exm_url')])

import pandas as pd 
df = pd.DataFrame(total).transpose()
df.to_clipboard() 