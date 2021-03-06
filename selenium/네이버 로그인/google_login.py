from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\chromedriver.exe')
 
driver.get('https://stackoverflow.com/') 
time.sleep(0.5) 
driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click() 
time.sleep(0.5) 
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click() 
time.sleep(0.5) 
driver.find_element_by_id('identifierId').send_keys('skytreesea') 
driver.find_element_by_xpath( '//*[@id="identifierNext"]/div/button/div[2]').click() 
time.sleep(2)
 