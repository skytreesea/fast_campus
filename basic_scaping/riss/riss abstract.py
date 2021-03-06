from bs4 import BeautifulSoup 
import requests, re, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 여기에 다운 받아 크롬 브라우저드라이버 실행파일의 주소를 입력하세요. 
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\chromedriver.exe')
basic = 'http://www.riss.kr'
# 키워드만 바꿔가면서 넣으면 됨
url = 'https://www.dbpia.co.kr/search/topSearch?startCount=0&collection=ALL&range=A&searchField=ALL&sort=RANK&query=%EC%A7%80%EB%B0%A9%EA%B3%B5%EA%B8%B0%EC%97%85&srchOption=*&includeAr=false'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
driver.get(url)
print([i.find('a').get('href') for i in driver.find_elements_by_class_name('titWrap')])
