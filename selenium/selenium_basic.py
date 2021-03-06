# 키워드만 바꿔가면서 넣으면 됨
from selenium import webdriver
#키를 입력하기 위해서 필요한 모듈
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\chromedriver.exe')
url = 'https://comic.naver.com/index.nhn'
driver.get(url)
for i in driver.find_elements_by_id('genreRecommand'):
    try:
        print(i.text, i.get_attribute('href'))
    except:
        pass