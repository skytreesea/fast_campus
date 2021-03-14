import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
url = 'https://datalab.naver.com/keyword/realtimeList.naver?age=40s'
age = ['10대','20대','30대','40대']
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\chromedriver.exe') 
# driver.get(url)
# total = []
# for i in age:
#     driver.find_element_by_link_text(i).click()
#     total.append([i.text for i in driver.find_elements_by_class_name('item_title')][5:])

# import pandas 
# df = pandas.DataFrame(total).transpose()
# df.to_clipboard()
category = ['댓글수','작성자수','섹션별 분포','시간대별 분포','성별,연령별 분포','기기별 분포','국가별 분포']
driver.get('https://datalab.naver.com/commentStat/news.naver')
driver.maximize_window()
for i in category:
    driver.find_element_by_link_text(i).click()
    body = driver.find_element_by_tag_name('body')
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(5)
    driver.save_screenshot(r'C:\Users\ERC\Pictures\Saved Pictures\스크린샷\\'+i+'.png')