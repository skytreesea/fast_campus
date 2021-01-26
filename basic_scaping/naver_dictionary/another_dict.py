#네이버 사전 예문 크롤링 기본형
import os , re, datetime, random, csv
import requests
from bs4 import BeautifulSoup 
# words를 늘리면 단어 뜻과 예문 출력이 가능함
words=['example','greatest','vindictive','patriotic','strategy','abundant','adjacent']
# 아래 주소에 단어만 더하면 단어 뜻과 예문이 든 페이지로 이동
url = 'https://dic.daum.net/search.do?q=crawling'
def bs(url):
    return BeautifulSoup(requests.get(url).text,'lxml')

soup = bs(url)
for i in soup.find_all('ul',{'class':'list_search'}):
    print([j.text for j in i.find_all('li')]) 
    
for i in soup.find_all('a',{'class':'txt_cleansch'}):
    soup2 = bs('https://dic.daum.net/'+i.get('href'))

for i in soup2.find_all('span',{'class','txt_ex'}):
    print(i.text)