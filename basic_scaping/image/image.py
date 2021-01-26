#구글 특정이미지 크롤링
import os, re, datetime, random, csv
import requests, time
from bs4 import BeautifulSoup as bs
imgname='seoul'
url = 'https://www.google.com/search?q={}&newwindow=1&rlz=1C1CAFC_koKR919KR919&sxsrf=ALeKk01PWz-3zrCezKvFVvXxnrJkKFPuFA:1611643217401&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjb_Ojr_rjuAhVZIqYKHRCAAqMQ_AUoAXoECAEQAw&biw=1555&bih=984'.format(imgname)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = bs(requests.get(url, headers = headers).text, 'lxml')     

os.chdir(r'C:\Users\ERC\Pictures\Saved Pictures')
k=0
#특정 사이트 접속
for i in soup.find_all('a', {'class':'VFACy kGQAp sMi44c lNHeqe WGvvNb'})[:50]:
    try:
        url2 = i.get('href')
        soup = bs(requests.get(url2, headers = headers).text, 'lxml')      
        k=0
        for i in soup.find_all('img'):
            print(i.get('src'))
            #특정사이트에서 이미지 모두 가져옴
            with open(imgname+ str(k) +'.jpg','wb') as b :
                b.write(requests.get(i.get('src')).content)
            k +=1 
    except:
        pass