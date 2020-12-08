# 인기글 스크래핑 제목 성공
import requests, re, time, csv
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 신규 크롤링
url = 'http://www.saramin.co.kr/zf_user/jobs/public/list?sort=ud&quick_apply=&search_day=&keyword=&company_scale%5B%5D=4#listTop'
soup = bs(requests.get(url).text, 'html.parser')
company_name = soup.find_all('td', {'class':'company_nm'})
deadline = soup.find_all('p', {'class':'deadlines'})
detail = soup.find_all('a', {'class':'str_tit'})
employment_type = soup.find_all('p', {'class':'employment_type'})

saramin = []
for num in range(len(company_name)):
    try:
        saramin.append([company_name[num].text, deadline[num].text,detail[num].text, employment_type[num].text,'http://www.saramin.co.kr'+detail[num].get('href')])
    except:
        pass
    #'http://www.saramin.co.kr'+detail[num].get('href')])

def writecsv(filename, the_list):
    #브라보 utf-8-sig: 대단한 발견
    with open(filename,'w', newline='', encoding='utf-8-sig') as f:
        a=csv.writer(f, delimiter=',')
        a.writerows(the_list)

writecsv('saramin_public.csv', saramin)