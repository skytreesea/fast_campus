# stocktoday에서 csv파일 가져와서 각 제목을 크롤링 하는 데 성공 
from bs4 import BeautifulSoup as bs
import requests, re, usecsv, datetime, os
# stocktoday= usecsv.opencsv('stocktoday1220.csv')
# url = stocktoday[0][1]
# os.chdir(r'C:\Users\ERC\Documents\GitHub\fast_campus\basic_scaping\stock')
# f = open('stocktalk.txt','w',encoding='utf8')
for url in stocktoday[:2]:
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    soup = bs(requests.get(url[1], headers = headers).text, 'lxml')
    print(url[0])
    #sub_section right에는 두 개의 요소가 있었음 위, 아래, 우리는 아래 것을 크롤링
    for i in soup.find_all('div', {'class':'sub_section right'})[1].find_all('li'):
        # f.write(i.find('a').text)
        post = 'https://finance.naver.com'+i.find('a').get('href')
        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
        soup2 = bs(requests.get(post, headers = headers).text, 'lxml')
        print(soup2.find('div', {'id':'body'}).text)
        # f.write(soup2.find('div', {'id':'body'}).text)
# f.close()
