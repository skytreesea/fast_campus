from bs4 import BeautifulSoup
import requests, re
url = 'https://finance.naver.com/item/main.nhn?code=035080'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
def get_img(url):
    soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')
    with open(r'C:\Users\ERC\Pictures\Saved Pictures\\'+url[-7:]+'.jpg','wb') as f :
        f.write(requests.get(soup.find('img',{'id':'img_chart_area'}).get('src')).content)

get_img(url)