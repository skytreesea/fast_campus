# 인기글 스크래핑 제목 성공
import requests, re, time, csv
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 신규 크롤링
url = 'http://www.saramin.co.kr/zf_user/jobs/public/list'
a_sample='https://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=39455251&recommend_ids=eJxdj8kRA0EIA6Pxn0MgeDuQzT8LX7PDlJ9NU0J4R0t7XtHx4NMPvPAbuJXhInKhAh%2F%2Fj%2Fd6iga2h6QEZ500%2BIQFsg%2B7cYcp1MZvXP6dX17jW0zkfGXhWkeFh0w3MDiveLeB0w1E1SAtXQ9ban1jsTJ0Jxffp6hHL03W7gUz1PfuCydNVFY%3D&view_type=list&gz=1&t_ref_content=education&t_ref=hot100#seq=0'
soup = bs(requests.get(a_sample).text, 'html.parser') 
time.sleep(5)
print(soup.find('div',{'class':'status'}))
