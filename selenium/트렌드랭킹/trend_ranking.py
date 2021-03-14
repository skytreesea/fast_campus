import time
#셀레니움 기본 작동을 위해서 필요한
from selenium import webdriver
#키를 입력하기 위해서 필요한 모듈
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
# 급상승 검색어 연령별로 선택하여 저장
url = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=2021-03-14T05:59:30'
# 셀레니움으로 접근
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\chromedriver.exe')
# age= ['10대', '20대','30대','40대']
# total = []
# for j in age:
#     driver.get(url)
#     time.sleep(2)
#     driver.find_element_by_link_text(j).click()
#     time.sleep(2)
#     total.append([i.text for i in driver.find_elements_by_class_name('item_title')])

# import pandas as pd 
# df = pd.DataFrame(total).transpose()
# df.to_clipboard()

links = ['댓글수', '작성자수', '섹션별 분포','시간대별 분포','성별,연령별 분포','기기별 분포','국가별 분포']
driver.get(url)
time.sleep(2)
driver.find_element_by_link_text('뉴스댓글통계').click()

for j in links:
    driver.find_element_by_link_text(j).click()
    body = driver.find_element_by_tag_name('body')
    body.send_keys(Keys.PAGE_DOWN)
    driver.maximize_window()
    time.sleep(2)
    driver.save_screenshot(r'C:\Users\ERC\Pictures\Saved Pictures\스크린샷\\' +j+'뉴스 댓글통계.png')

