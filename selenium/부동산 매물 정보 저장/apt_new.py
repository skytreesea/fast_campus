# 아파트 들어가 아파트 이름, 주소, 정보까지 출력하는데 성공, csv화는 미성공
import time 
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\chromedriver.exe')
driver.get('https://land.naver.com/')
apt ='은마'