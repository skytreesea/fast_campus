import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 여기에 다운 받아 크롬 브라우저드라이버 실행파일의 주소를 입력하세요. 
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\chromedriver.exe')

basic = 'https://map.naver.com/v5/directions/-/-/-/transit?c=14140822.8268590,4508397.7630627,15,0,0,0,dh'

def route(start, finish):
    driver.get(basic)
    # 3초정도 멈추었다가 진행
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div[1]/ul/li[2]/a').click()
    # 3초정도 멈추었다가 진행
    time.sleep(3)
    # 시작점
    startx = driver.find_element_by_xpath('//*[@id="directionStart0"]')
    startx.send_keys(start)
    startx.send_keys(Keys.RETURN)
    time.sleep(3)
    # 끝 점
    finishx = driver.find_element_by_xpath('//*[@id="directionGoal1"]')
    finishx.send_keys(finish)
    finishx.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div/directions-search/div[2]/button[3]').click()
    time.sleep(3)
    print(driver.find_element_by_class_name('summary_box').text)
    time.sleep(3)
    driver.save_screenshot(r'C:\Users\ERC\Pictures\Saved Pictures\스크린샷\\'+start +finish +'.png')

route('강남역', '연세대학교')