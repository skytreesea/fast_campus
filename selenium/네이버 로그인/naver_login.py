# 네이버 로그인 성공
import pyperclip
import time
#셀레니움 기본 작동을 위해서 필요한
from selenium import webdriver
#키를 입력하기 위해서 필요한 모듈
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\패스트캠퍼스\자료\크롤링\selenium\chromedriver.exe')
driver.get('http://nid.naver.com/nidlogin.login')

xpath2 = '//input[@id="id"]' 
xpath3 = '//input[@id="pw"]'
xpath4 = '//input[@id="log.login"]'

my_id = 'skytreesea'
my_pw = 'kiss1124##'

# 크롬창 켜기
pyperclip.copy(my_id) # id 복사
driver.find_element_by_xpath(xpath2).send_keys(Keys.CONTROL, 'v') # id 붙여넣기
pyperclip.copy(my_pw) # 비밀번호 복사
driver.find_element_by_xpath(xpath3).send_keys(Keys.CONTROL, 'v') # 비밀번호 붙여넣기
driver.find_element_by_xpath(xpath4).click() # 로그인 클릭
