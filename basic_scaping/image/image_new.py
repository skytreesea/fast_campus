import requests 
from bs4 import BeautifulSoup  
# 키 바꾸면 다른 사진도 모을 수 있음 
key = '런던'
url = 'https://ko.wikipedia.org/wiki/' + key 
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = BeautifulSoup(requests.get(url, headers = headers).text,'lxml') 
basic = 'https://ko.wikipedia.org'
k = 0
# 
for j in soup.find_all('div',{'class':'thumbinner'}):
    soup2 = BeautifulSoup(requests.get(basic + j.find('a').get('href'), headers = headers).text,'lxml')
    # http 꼭 붙여주기 
    nurl = 'https:' + soup2.find('div',{'class':'fullImageLink'}).find('a').get('href')
    print(nurl)
    # 기본명령부터 시작 
    with open(r'C:\Users\ERC\Pictures\사진 저장 폴더\\'+ key + str(k)+ '.jpg', 'wb') as f:
        f.write(requests.get(nurl).content)
    k+=1 
