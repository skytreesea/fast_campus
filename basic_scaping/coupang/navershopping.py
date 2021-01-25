# 뷰티풀수프 상용어구
from bs4 import BeautifulSoup  
import requests, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 중요: 크롬드라이브를 다운받은 경로를 따와서 그대로 입력합니다.
driver = webdriver.Chrome(r'D:\user\Documents\git hub\fast_campus\selenium\chromedriver.exe')
url='https://search.shopping.naver.com/search/all?query=%EC%97%AC%EC%9E%90%EC%A7%80%EA%B0%91&cat_id=&frm=NVSHATC' 
driver.get(url)
driver.implicitly_wait(10)
def makeSoup(url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(url, headers = headers)
    return BeautifulSoup(res.text, 'lxml') 
time.sleep(3)
body = driver.find_element_by_tag_name('body')
# body를 스크롤합니다. tagname이 body로 되어있는것을 추출합니다. 이해 어려우면 그냥 따라해도 됩니다. 
pagedowns =0
# 페이지 다운을 몇 번 할지 정해줍니다. 
while pagedowns < 5:
    body.send_keys(Keys.PAGE_DOWN)
    pagedowns +=1
  # Selenium이 페이지 다운을 할 수 있도록 코드를 입력합니다.
    time.sleep(2)
  # 스크롤을 하고 화면이 뜨도록 시간을 둡니다.

soup = makeSoup(url)
for i in soup.find_all('div',{'class':'basicList_info_area__17Xyo'}):
    try:
        print('제품명', i.find('div',{'class':'basicList_title__3P9Q7'}).text)
    except:
        pass
