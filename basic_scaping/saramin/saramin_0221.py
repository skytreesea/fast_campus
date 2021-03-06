# 인기글 스크래핑 제목 성공
# 뷰티풀 숩과 requests 임포트 
import requests 
from bs4 import BeautifulSoup  
# 판다스 임포트
import pandas as pd
# 신규 크롤링
url = 'https://www.saramin.co.kr/zf_user/?NaPm=ct%3Dklei7qaa%7Cci%3Dcheckout%7Ctr%3Dds%7Ctrx%3D%7Chk%3D687964c1afb2019919f802e35c1eebfcca0ef184'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')

data = []
for i in soup.find_all('div',{'class':'box_product'}):
    data.append([i.find('strong',{'class':'poduct_tit'}).text,[j.text for j in i.find_all('em')],[j.text for j in i.find_all('span',{'class':'wrap_desc'})]])

df = pd.DataFrame(data)
df.to_clipboard()
