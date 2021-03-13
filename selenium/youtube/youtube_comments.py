# 유튜브 비디오에서 댓글 가져오기 예제: 성공, 스크롤 내린 후 뷰티풀 수프로 긁어오기
import requests, time 
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\chromedriver.exe')
driver.get('https://www.youtube.com/watch?v=2MgVkjMZGwc')
time.sleep(3)

body = driver.find_element_by_tag_name('body')
down = 0
while down < 5: 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    down += 1

soup = BeautifulSoup(driver.page_source, 'lxml')
print([i.text for i in soup.find_all('div',{'class':'style-scope ytd-expander'})])