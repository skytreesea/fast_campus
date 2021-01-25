from bs4 import BeautifulSoup  
import requests,re

basic = 'https://www.coupang.com'
url = 'https://www.coupang.com/np/search?component=&q=%EB%AC%B4%EB%A6%8E%EB%8B%B4%EC%9A%94&channel=user' 
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'lxml')

total =[]
for i in soup.find_all('dd',{'class':'descriptions'}):
    try:
        k =[i.find('div',{'class':'name'}).text,
        i.find('strong',{'class':'price-value'}).text,
        i.find('em',{'class':'rating'}).text,
        i.find('span',{'class':'rating-total-count'}).text,
        i.find_all('a').get('href')]
        total.append(k)
    except: 
        pass
print(total)
import pandas as pd 
pd.DataFrame(total).to_clipboard()
# for i in soup.find_all('strong',{'class':'price-value'}):
#     print(i.text)

# for i in soup.find_all('em',{'class':'rating'}):
#     print(i.text)

# for i in soup.find_all('span',{'class':'rating-total-count'}):
#     print(i.text) 