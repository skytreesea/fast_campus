import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

basic = 'https://new.land.naver.com/complexes/236?ms=37.497811,127.06502,17&a=APT:ABYG:JGC&e=RETAIL'
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\chromedriver.exe')
driver.get(basic)
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="complexOverviewList"]').click() # 이 부분 선택이 중요

time.sleep(1)
driver.find_element_by_tag_name('body').send_keys(Keys.END)   
time.sleep(1)
driver.find_element_by_tag_name('body').send_keys(Keys.END)   
time.sleep(1)
driver.find_element_by_tag_name('body').send_keys(Keys.END)    