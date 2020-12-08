#네이버 로그인 시도 실패
import time
#chrome 버젼 87.0.4280.88
from selenium import webdriver
#글자를 가져오기 위해서는 다음 
from selenium.webdriver.common.keys import Keys
# 자동으로 닫히지 않게 하기 위해서 
from selenium.webdriver.chrome.options import Options
browser = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\패스트캠퍼스\자료\크롤링\selenium\chromedriver.exe')
browser.get('http://www.naver.com')
#주의할 점 selenium이라고 파일 이름 정하면 안됨 
#오류에서 벗어나는 방법
elem = browser.find_element_by_class_name('link_login')
elem.click()
#browser.back()
#browser.forward()
id = 'skytreese'
real_id = 'skytreesea'
pw = 'kiss1124##'
#browser.refresh()
register = browser.find_element_by_id('id').send_keys(id)
register = browser.find_element_by_id('pw').send_keys(pw)
register = browser.find_element_by_id('log.login').click()

#일단 성공함 그러나 자동 로그인 방지 장치를 만들어놓음
time.sleep(5)

register.find_element_by_id('id').clear()
register.find_element_by_id('id').send_keys(real_id)
register = browser.find_element_by_id('pw').send_keys(pw)
register = browser.find_element_by_id('log.login').click()

#자동으로 닫히지 않게 하기 위해서 필요 
#chrome_options.add_experimental_option("detach", True)
#탭 닫기
#browser.close()
#전체 브라우저 닫기 
#browser.quit()
#네이버 자동 로그인
