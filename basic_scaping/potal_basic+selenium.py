#네이버 메인에 있는 주요 글들 출처와 내용의 일부를 크롤링하기
import requests, time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url='https://www.naver.com/'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = bs(requests.get(url, headers = headers).text, 'lxml')
#링크들 저장하기 위한 리스트 
hrefs=[]
#윈도우즈 저장을 위한 명령어 두 줄 
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\chromedriver.exe')
driver.get(url)    
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
for i in driver.find_elements_by_class_name('theme_item'):
    i.send_keys(Keys.CONTROL, '\n')
    

