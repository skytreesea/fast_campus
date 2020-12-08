# 클리앙 인기글 스크래핑 제목 성공
import requests, re, time, csv
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url = 'https://www.clien.net/service/'
soup = bs(requests.get(url).text, 'html.parser')
bestarticles=[]
for i in soup.find_all('div', {'class':'section_body'}):
    #for j in i.find_all('span',{'class':'subject'}):
    for j in i.find_all('a'):
        bestarticles.append([re.sub(r'\\','',j.text),'https://www.clien.net'+j.get('href')])
#한글로 저장 안되는 문제 해결해야 
def writecsv(filename, the_list):
    #브라보 utf-8-sig: 대단한 발견
    with open(filename,'w', newline='', encoding='utf-8-sig') as f:
        a=csv.writer(f, delimiter=',')
        a.writerows(the_list)

writecsv('clien_py_suc.csv',bestarticles)
