# 네이버 로그인 성공
import pyperclip
import time
#셀레니움 기본 작동을 위해서 필요한
from selenium import webdriver
#키를 입력하기 위해서 필요한 모듈
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\패스트캠퍼스\자료\크롤링\selenium\chromedriver.exe')
driver.maximize_window()

url='https://www.google.co.kr/imghp?hl=ko'
driver.get(url)
driver.find_element_by_name('q').click()

 