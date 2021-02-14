# 인기글 스크래핑 제목 성공
import requests, re, time, csv
from bs4 import BeautifulSoup as bs

# 신규 크롤링
url = 'https://www.saramin.co.kr/zf_user/jobs/list/domestic?loc_mcd=106000'
soup = bs(requests.get(url).text, 'html.parser')
time.sleep(3)
print(soup.find('ul', {'class':'product_list unit_list'}).find_all('li'))