import time
import pyperclip
#셀레니움 기본 작동을 위해서 필요한
from selenium import webdriver
#키를 입력하기 위해서 필요한 모듈
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\chromedriver.exe')
url = 'https://nid.naver.com/nidlogin.login'
driver.get(url)
id = '//*[@id="id"]'
pw = '//*[@id="pw"]'
button = '//*[@id="log.login"]'

my_id = 'fast_stranger'
my_pw = 'muscle1234$$' 

pyperclip.copy(my_id)
driver.find_element_by_xpath(id).send_keys(Keys.CONTROL,'v')

pyperclip.copy(my_pw)
driver.find_element_by_xpath(pw).send_keys(Keys.CONTROL,'v')
driver.find_element_by_xpath(button).click()
time.sleep(3)
driver.get('https://mail.naver.com/')