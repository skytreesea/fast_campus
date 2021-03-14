import time
# 크롬 브라우저를 띄우기 위해, 웹드라이버를 가져오기
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
url ='http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?area=&bidNm=%BF%AC%B1%B8&bidSearchType=1&fromBidDt=2021%2F02%2F12&fromOpenBidDt=&instNm=&maxPageViewNoByWshan=4&radOrgan=1&regYn=Y&searchDtType=1&searchType=1&taskClCds=&toBidDt=2021%2F03%2F14&toOpenBidDt=&currentPageNo=1'

soup = BeautifulSoup(requests.get(url).text, 'lxml')
links = [i.find('a').get('href') for i in soup.find_all('td',{'class':'tl'}) if i.find('a')]

total =[]
# 각 요소들을 판다스로 불러오기 
for item in links[:5]:
    try:
        driver = webdriver.Chrome(r'C:\Users\ERC\Documents\chromedriver.exe')
        driver.get(item)
        total.append([i.text for i in driver.find_elements_by_class_name('tb_inner')])
        time.sleep(2)
    except: 
        pass

import pandas as pd 
df = pd.DataFrame(total)
df.to_clipboard()