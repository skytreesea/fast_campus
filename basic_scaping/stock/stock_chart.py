# stocktoday에서 csv파일 가져와서 각 제목을 크롤링 하는 데 성공 
from bs4 import BeautifulSoup  
import requests, re, usecsv, datetime, os
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
#브레인콘텐츠 url을 가져옴
# stocktoday= usecsv.opencsv('stocktoday1220.csv')
urls=['https://finance.naver.com//item/main.nhn?code=033170','https://finance.naver.com//item/main.nhn?code=036630', 'https://finance.naver.com//item/main.nhn?code=036540']
#차트 이미지 다운받기 성공
os.chdir(r'C:\Users\ERC\Pictures\Saved Pictures')
for url in urls:
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')
    for i in soup.find_all('div', {'class':'chart'}):
        # 주식종목만 입력하면 차트 자동 다운로드
        with open(url[-6:]+'chart.jpg', 'wb') as handler:
            handler.write(requests.get(i.find('img').get('src')).content)
