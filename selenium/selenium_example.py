# 유튜브 비디오 관련영상 제목 출력
import requests, re, time 
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
keyword='웹크롤링'
driver = webdriver.Chrome(r'D:\user\Documents\git hub\fast_campus\selenium\chromedriver.exe')
driver.get('https://www.youtube.com/results?search_query='+keyword)
time.sleep(3)
video_list = driver.find_elements_by_id('video-title')

for video in video_list: 
    print(video.text)