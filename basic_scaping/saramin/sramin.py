import requests 
from bs4 import BeautifulSoup 
url = 'https://www.saramin.co.kr/zf_user/jobs/hot100'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

total = []
total.append([i.text for i in soup.find_all('a', {'class':'company_name'})]) 
total.append([i.text for i in soup.find_all('a', {'class':'tit'})]) 

import pandas
df = pandas.DataFrame(total).transpose()
df.to_clipboard()