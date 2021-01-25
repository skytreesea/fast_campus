# 유튜브 비디오 관련영상 제목 출력
import requests, re, time 
from bs4 import BeautifulSoup  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url='https://search.shopping.naver.com/search/all?catId=50003990&frm=NVSHCAT&origQuery=%EC%95%BC%EA%B5%AC%EB%AA%A8%EC%9E%90&pagingIndex=1&pagingSize=40&productSet=total&query=%EC%95%BC%EA%B5%AC%EB%AA%A8%EC%9E%90&sort=rel&timestamp=&viewType=list' 

def makeSoup(url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(url, headers = headers)
    return BeautifulSoup(res.text, 'lxml') 

soup = makeSoup(url)
for i in soup.find_all('div',{'class':'basicList_title__3P9Q7'}):
    print(i.text)
    # print(i.find('a'))