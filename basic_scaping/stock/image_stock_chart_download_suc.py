# stocktoday에서 csv파일 가져와서 그 안에 있는 url 정보만으로 챠트 이미지 저장하기 성공
from bs4 import BeautifulSoup as bs
import requests, re, usecsv, datetime, os
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
#애이프로바이오 url을 가져옴
stocktoday= usecsv.opencsv('stocktoday1220.csv')
#차트 이미지 다운받기 성공
os.chdir(r'C:\Users\ERC\Documents\GitHub\fast_campus\basic_scaping\stock\img')
# stocktoday url 모두에서 찾아서 자동으로 챠트 이미지 다운로드 받기  
for url in stocktoday:
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    soup = bs(requests.get(url[1], headers = headers).text, 'lxml')
    for i in soup.find_all('div', {'class':'chart'}):
        #주식이름 url[0]을 이름으로 하는 jpg 파일명 생성
        with open(url[0]+'chart.jpg', 'wb') as handler:
            # img에서 src라는 요소 찾아서 requests로 불러낸 후 그것의 content를 파일에 쓰라고 명령
            handler.write(requests.get(i.find('img').get('src')).content)
 