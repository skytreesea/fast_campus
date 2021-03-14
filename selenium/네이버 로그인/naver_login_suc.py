# 네이버 로그인 성공
import pyperclip
import time
#셀레니움 기본 작동을 위해서 필요한
from selenium import webdriver
#키를 입력하기 위해서 필요한 모듈
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\chromedriver.exe')
driver.get('http://nid.naver.com/nidlogin.login')

xpath2 = '//input[@id="id"]' 
xpath3 = '//input[@id="pw"]'
xpath4 = '//input[@id="log.login"]'

my_id = 'fast_stranger'
my_pw = 'muscle1234$$' 

# 크롬창 켜기
pyperclip.copy(my_id) # id 복사
driver.find_element_by_xpath(xpath2).send_keys(Keys.CONTROL, 'v') # id 붙여넣기
pyperclip.copy(my_pw) # 비밀번호 복사
driver.find_element_by_xpath(xpath3).send_keys(Keys.CONTROL, 'v') # 비밀번호 붙여넣기
driver.find_element_by_xpath(xpath4).click() # 로그인 클릭
time.sleep(3)
driver.get('https://mail.naver.com/')
names = driver.find_elements_by_class_name('subject ')

# 메일 제목만 출력하기
for i in names:
    print(i.text)
# 메일 내용 들어가보기  
for i in names:
    driver.switch_to_window(driver.window_handles[1])

