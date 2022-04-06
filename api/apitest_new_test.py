import requests,re, json
from bs4 import BeautifulSoup
key = '7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D'
# PM10은 미세먼지, PM25는 초미세먼지 
url ='https://www.cleaneye.go.kr/user/openXmlMajorMngIdx.do?serviceKey=7JlKxM7fEbOErQRa32MtR3%2Fg%2FBxi3JTPbwPfCw781Ma4uvwql5x2r2wM0Zh051RRUK%2Bw7YSwijxr0Tklej3cOg%3D%3D&pageNo=1&numOfRows=50&ac_year=2017&type=xml&SG_APIM=2ug8Dm9qNBfD32JLZGPN64f3EoTlkpD8kSOHWfXpyrY'


# 해당 페이지에서 되는 url을 가져와서 이것 저것 바꿔보는 것이 가장 좋음
soup = BeautifulSoup(requests.get(url).text, 'lxml')
total = []
# 찾을 때는 소문자로 찾아야 함 
total.append([i.text for i in soup.find_all('AC_YEAR')])
total.append([i.text for i in soup.find_all('ENT_NAME')])

import pandas as pd 
df = pd.DataFrame(total).transpose()
df.to_clipboard() 

