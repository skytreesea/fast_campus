# 뷰티풀수프 상용어구
from bs4 import BeautifulSoup  
import requests 
url='https://search.shopping.naver.com/search/all?query=여자바지&cat_id=&frm=NVSHATC' 
def makeSoup(url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(url, headers = headers)
    return BeautifulSoup(res.text, 'lxml') 

soup = makeSoup(url)

for i in soup.find_all('div',{'class':'basicList_info_area__17Xyo'})[:50]:
    try:
        print('제품명', i.find('div',{'class':'basicList_title__3P9Q7'}).text)
        print('가격', i.find('span',{'class':'price_num__2WUXn'}).text)
        print('', i.find('span',{'class':'basicList_etc__2uAYO'}).text)
        print('찜하기', i.find('em',{'class':'basicList_num__1yXM9'}).text)
        # print(i.find('a',{'class':'basicList_compare__3AjuT'}).text)
    except:
        pass
