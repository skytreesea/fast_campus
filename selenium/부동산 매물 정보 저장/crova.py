# 크로바 아파트 들어가는 페이지까지만 성공
import requests, re, time 
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\패스트캠퍼스\자료\크롤링\selenium\chromedriver.exe')
driver.get('https://land.naver.com/')
apt ='크로바\n'
#크로바 아파트로 들어가는 데까지는 성공
driver.find_element_by_id('queryInputHeader').send_keys(apt) 
title = driver.find_elements_by_class_name('title')
address = driver.find_elements_by_class_name('address')
info = driver.find_elements_by_class_name('info_area')
for i in range(len(title)):
    print(title[i].text, address[i].text, info[i].text)