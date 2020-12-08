# 인기글 스크래핑 제목 성공
import requests, re, time, csv
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 신규 크롤링
url = 'https://hibrain.net/recruitment/recruits?listType=D3NEW'
soup = bs(requests.get(url).text, 'html.parser')
name = soup.find_all('span', {'class':'title titleImageNone'})
date = soup.find_all('span', {'class':'td_receipt'}) 

new_recruit = []
for i in range(len(name)):
    new_recruit.append([name[i].text, date[0].text])

def writecsv(filename, the_list):
    #브라보 utf-8-sig: 대단한 발견
    with open(filename,'w', newline='', encoding='utf-8-sig') as f:
        a=csv.writer(f, delimiter=',')
        a.writerows(the_list)

writecsv('hibrain_new_1207.csv', new_recruit)