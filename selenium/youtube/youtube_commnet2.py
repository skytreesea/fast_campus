# 유튜브 비디오에서 댓글 가져오기 예제: 성공, 스크롤 내린 후 뷰티풀 수프로 긁어오기
import requests, re, time 
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\chromedriver.exe')
driver.get('https://www.youtube.com/watch?v=2MgVkjMZGwc')

time.sleep(3)
body = driver.find_element_by_tag_name('body')

pagedowns = 0
while pagedowns < 5:
  body.send_keys(Keys.PAGE_DOWN)
  # Selenium이 페이지 다운을 할 수 있도록 코드를 입력합니다.
  time.sleep(1)
  # 스크롤을 하고 화면이 뜨도록 시간을 둡니다.
  pagedowns +=1
 
soup = bs(driver.page_source, 'lxml')
# commment를 직접 F12를 눌러 찾아야 합니다
comments = [i.text for i in soup.find_all('div',{'class':'style-scope ytd-expander'})]
for i in comments:
  print(i)
#댓글단 사람들 유튜브 채널 모두 열어보기 
for i in soup.find_all('div',{'class':'style-scope ytd-comment-renderer'})[:5]:
    news = driver.find_elements_by_id('author-text')
    try:
        new = 'https://www.youtube.com'+i.find('a').get('href')
    except:
        pass
news = driver.find_elements_by_id('author-text')
# 다섯명의 유튜버만 페이지 열어보기 
for i in news[:10]:
    i.send_keys(Keys.CONTROL +"\n")  