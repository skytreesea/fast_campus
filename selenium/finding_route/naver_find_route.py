# 네이버 지도 길 찾기 결과 검색하기 
import requests, re, time 
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 여기에 크롬 브라우저드라이버의 주소를 입력하세요. 
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\chromedriver.exe')
driver.get('https://map.naver.com/v5/directions/-/-/-/transit?c=14139268.8290314,4507639.6434387,15,0,0,0,dh')
# 시작하는 지점과 끝을 입력하세요. 
start = '신대방'
finish = '지방공기업평가원'
# 불러오는 시간이 있으니 약간의 딜레이를 줍니다. 
time.sleep(3)
# 자동차 거리를 선택합니다. 
driver.find_elements_by_class_name('item_tab')[1].click()
time.sleep(1)
# 시작하는 지점을 입력하고 엔터치도록 해줍니다. 
el = driver.find_element_by_id('directionStart0')
el.send_keys(start)
el.send_keys(Keys.RETURN)
time.sleep(1)
# 끝나는 지점을 입력하고 엔터치도록 해줍니다. 
el = driver.find_element_by_id('directionGoal1')
time.sleep(1)
el.send_keys(finish)
el.send_keys(Keys.RETURN)
time.sleep(1)
el.send_keys(Keys.RETURN)
time.sleep(2)
# 루트 정보를 찾아 입력하도록 합니다.
group = driver.find_elements_by_class_name('route_title') 
time.sleep(2)
for i in group:
    print(i.text)
# 추천 시간을 출력하도록 해줍니다. 
result = driver.find_element_by_class_name('summary_box')
print(result.text)
