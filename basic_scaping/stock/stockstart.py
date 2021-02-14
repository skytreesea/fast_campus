from bs4 import BeautifulSoup
import requests
basic = 'https://finance.naver.com'
url = 'https://finance.naver.com/main/main.nhn'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')

k = range(1,5)
b= []
for j in k:
    for i in soup.find_all('tbody',{'id':'_topItems'+str(j)}):
        try:
            for j in i.find_all('th'):
                new = [j.find('a').text, basic  + j.find('a').get('href')]
                b.append(new)
        except:
            pass
        
import pandas as pd

df = pd.DataFrame(b)
df.to_clipboard()