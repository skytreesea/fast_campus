# 인기글 스크래핑 제목 성공
import requests 
from bs4 import BeautifulSoup 

# 신규 크롤링
url = 'http://www.saramin.co.kr/zf_user/jobs/hot100'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
company_name = soup.find_all('a', {'class':'company_name'})
detail = soup.find_all('a', {'class':'tit'})

saramin = []
#     print('http://www.saramin.co.kr'+detail[num].get('href'))
for num in range(len(company_name)):
    saramin.append([company_name[num].text, detail[num].text, 'http://www.saramin.co.kr'+detail[num].get('href')])

import pandas as pd 
df = pd.DataFrame(saramin)
df.to_clipboard()