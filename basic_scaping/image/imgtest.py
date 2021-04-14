import requests
from bs4 import BeautifulSoup
key = '아이유'
# 위키피디아 항목의 url
url = 'https://ko.wikipedia.org/wiki/' + key
# with open(r'C:\Users\ERC\Pictures\사진 저장 폴더\\뉴욕연습.jpg', 'wb') as f:
#     f.write(requests.get(url).content)
basic = 'https://ko.wikipedia.org'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = BeautifulSoup(requests.get(url, headers = headers).text,'lxml') 
k = 0 
for i in soup.find_all('div',{'class':'thumbinner'}):
    newurl = basic + i.find('a').get('href')
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    soup2 = BeautifulSoup(requests.get(newurl, headers = headers).text,'lxml') 
    srcimg = 'https:' + soup2.find('div',{'class':'fullImageLink'}).find('a').get('href')
    
    with open(r'C:\Users\ERC\Pictures\사진 저장 폴더\\뉴욕{}.jpg'.format(str(k)), 'wb') as f:
        f.write(requests.get(srcimg).content)
    k += 1
 