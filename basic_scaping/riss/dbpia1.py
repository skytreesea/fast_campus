from bs4 import BeautifulSoup 
import requests, re, time
from selenium import webdriver
#키를 입력하기 위해서 필요한 모듈
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\chromedriver.exe')
url = 'https://www.dbpia.co.kr/search/topSearch?startCount=0&collection=ALL&range=A&searchField=ALL&sort=RANK&query=지방공기업&srchOption=*&includeAr=false'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
# url  = 'https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09407498'
soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')
driver.get(url)
# 키워드만 바꿔가면서 넣으면 됨

# headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
# url  = 'https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09407498'
# soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')
# print(soup.find('div',{'class':'quoteWrap'}).text)
# print(soup.find('p',{'class':'article'}))