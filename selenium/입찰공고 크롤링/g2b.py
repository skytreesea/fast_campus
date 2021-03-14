import time
# 크롬 브라우저를 띄우기 위해, 웹드라이버를 가져오기
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
# 크롬 드라이버로 크롬을 실행한다.
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\chromedriver.exe')
basic = 'http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?searchType=1&bidSearchType=1&taskClCds=&bidNm=%BF%AC%B1%B8&searchDtType=1&fromBidDt=2021%2F02%2F12&toBidDt=2021%2F03%2F14&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&instSearchRangeType=&refNo=&area=&areaNm=&industry=&industryCd=&budget=&budgetCompare=UP&detailPrdnmNo=&detailPrdnm=&procmntReqNo=&intbidYn=&regYn=Y&recordCountPerPage=30'

soup = BeautifulSoup(requests.get(basic).text,'lxml')
new = [i.find('a').get('href') for i in soup.find_all('td') if i.find('a')]
total = []
for j in new[3:10]:
    driver.get(j)
    total.append([i.text for i in driver.find_elements_by_class_name('tb_inner')][5:20])

import pandas as pd 
df = pd.DataFrame(total)
df.to_clipboard()