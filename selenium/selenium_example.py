# 네이버 지도 길 찾기 결과 검색하기 
import requests, re, time 
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\chromedriver.exe')
driver.get('https://map.naver.com/v5/directions/-/-/-/transit?c=14139268.8290314,4507639.6434387,15,0,0,0,dh')
start = '신대방역'
finish = '지방공기업평가원'
time.sleep(3)
driver.find_elements_by_class_name('item_tab')[1].click()
time.sleep(1)
el = driver.find_element_by_id('directionStart0')
el.send_keys(start)
el.send_keys(Keys.RETURN)
time.sleep(1)
el = driver.find_element_by_id('directionGoal1')
time.sleep(1)
el.send_keys(finish)
el.send_keys(Keys.RETURN)
time.sleep(1)
el.send_keys(Keys.RETURN)
time.sleep(2)
group = driver.find_elements_by_class_name('route_title') 

time.sleep(2)
for i in group:
    print(i.text)

result = driver.find_element_by_class_name('summary_box')
print(result.text)
