import time
#셀레니움 기본 작동을 위해서 필요한
from selenium import webdriver
#키를 입력하기 위해서 필요한 모듈
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
# 크롬 드라이버로 크롬을 실행한다. 가장 핵심은 url을 찾아야 한다는 점
url = 'http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?area=&bidNm=%BF%AC%B1%B8&bidSearchType=1&fromBidDt=2021%2F02%2F12&fromOpenBidDt=&instNm=&maxPageViewNoByWshan=2&radOrgan=1&regYn=Y&searchDtType=1&searchType=1&taskClCds=&toBidDt=2021%2F03%2F14&toOpenBidDt=&currentPageNo=1'
# driver = webdriver.Chrome(r'C:\Users\ERC\Documents\chromedriver.exe')
# driver.get(url)
soup = BeautifulSoup(requests.get(url).text, 'lxml')
new = [i.find('a').get('href') for i in soup.find_all('td',{'class':'tl'}) if i.find('a')]
new = list(set(new))
# print(new)

# 셀레니움으로 접근
total = []
for j in new:
    driver.get(j)
    total.append([i.text for i in driver.find_elements_by_class_name('tb_inner')])
 
import pandas as pd 
df = pd.DataFrame(total)
df.to_clipboard()