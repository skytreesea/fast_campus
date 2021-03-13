# 네이버 지도 길 찾기 결과 검색하기 
# 가장 먼저 할 일은 구글에서 크롬 드라이버를 다운받아 특정 폴더에 저장합니다. 
import requests, re, time 
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 여기에 다운 받아 크롬 브라우저드라이버 실행파일의 주소를 입력하세요. 
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\chromedriver.exe')

def route(start, finish):
    driver.get('https://map.naver.com/v5/directions/-/-/-/transit?c=14139268.8290314,4507639.6434387,15,0,0,0,dh')
    # 불러오는 시간이 있으니 약간의 딜레이를 줍니다. 
    time.sleep(3)
    # 자동차 거리를 선택합니다. 
    driver.find_element_by_xpath('/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div/ul/li[2]/a').click()
    time.sleep(1)
    # 시작하는 지점을 입력하고 엔터치도록 해줍니다. 
    el = driver.find_element_by_xpath('//*[@id="directionStart0"]')
    el.send_keys(start)
    el.send_keys(Keys.RETURN)
    time.sleep(3)
    el = driver.find_element_by_xpath('//*[@id="directionGoal1"]')
    el.send_keys(finish)
    el.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div/directions-search/div[2]/button[3]').click()
    time.sleep(3)
    print('{}에서 {}까지 걸리는 시간과 거리: {}\n'.format(start, finish, driver.find_element_by_class_name('summary_box').text))
    time.sleep(2)
    driver.save_screenshot(r'C:\Users\ERC\Pictures\Saved Pictures\스크린샷\\'+ start + finish+ '.png')

route('서울시청','경복궁')