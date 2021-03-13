# 크로바 아파트 들어가 아파트 이름, 주소, 정보까지 출력하는데 성공, csv화는 미성공
import requests, re, time, usecsv
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\chromedriver.exe')
driver.get('https://land.naver.com/')
#정상적으로 작동하게 하여 아파트 이름만 대도 갈 수 있도록 해야 
apt ='크로바\n'
#크로바 아파트로 들어가는 데까지는 성공
driver.find_element_by_id('queryInputHeader').send_keys(apt)
time.sleep(10) 
title = driver.find_elements_by_class_name('title')
address = driver.find_elements_by_class_name('address')
#find_elements로 정보를 모아서 text로 출력하게 하는 것이 핵심
info = driver.find_elements_by_class_name('info_area')
crova_list=[]
for i in range(len(title)):
    if title[i].text !='':
        try:
            crova_list.append([title[i].text, address[i].text, info[i].text])
        except:
            pass

usecsv.writecsv('crova_suc_sleep10.csv',crova_list)
