# 유튜브 비디오에서 댓글 가져오기 예제: 성공, 스크롤 내린 후 뷰티풀 수프로 긁어오기
import requests, re, time 
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 중요: 크롬드라이브를 다운받은 경로를 따와서 그대로 입력합니다.
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\chromedriver.exe')
body = driver.find_element_by_tag_name('body')
driver.get('https://www.youtube.com/watch?v=L_zjYgTbak8')
# driver.get('https://www.youtube.com/results?search_query='+keyword)
time.sleep(3)
body = driver.find_element_by_tag_name('body')
# body를 스크롤합니다. tagname이 body로 되어있는것을 추출합니다. 이해 어려우면 그냥 따라해도 됩니다. 
pagedowns = 10
# 페이지 다운을 몇 번 할지 정해줍니다. 
while pagedowns:
  body.send_keys(Keys.PAGE_DOWN)
  # Selenium이 페이지 다운을 할 수 있도록 코드를 입력합니다.
  time.sleep(2)
  # 스크롤을 하고 화면이 뜨도록 시간을 둡니다.
  pagedowns -= 1
# 스크롤 하는데 까지 성공
soup = bs(driver.page_source, 'lxml')
# commnet를 직접 F12를 눌러 찾아야 합니다
comments = soup.find_all('div',{'class':'style-scope ytd-expander'})

for comment in comments:
    print(comment)