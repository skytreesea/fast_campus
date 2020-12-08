from bs4 import BeautifulSoup as bs
import requests

url = ('https://m.blog.naver.com/PostView.nhn?blogId=popqser2&logNo=221229125022&proxyReferer=https:%2F%2Fwww.google.com%2F')
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = bs(res.text, 'lxml') 
for i in soup.find_all('div', {'class':'se_sectionArea'}).find('div', {'class':'textView'}):
        print(i.find_all('span'))