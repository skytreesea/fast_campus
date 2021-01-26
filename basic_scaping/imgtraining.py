# 뷰티풀수프 상용어구
from bs4 import BeautifulSoup  
import requests, time
def bs(url):
    return BeautifulSoup(requests.get(url).text,'lxml')       
basicurl = 'https://www.sisain.co.kr/news/articleList.html?sc_section_code=S1N14'
soup = bs(basicurl)

# print(soup.find_all('div',{'id':'article-view-content-div'}))
total = []
for i in soup.find_all('article',{'class':'items'}):
    total.append('https://www.sisain.co.kr'+i.find('a').get('href'))

# print(total)

for item in total:
    try:
        soup = bs(item)
        for i in soup.find_all('div',{'id':'article-view-content-div'}):
            with open(r'C:\Users\user\Pictures\Saved Pictures\\'+ item[-5:]+'.jpg','wb') as b:
                    b.write(requests.get('https://www.sisain.co.kr'+i.find('img').get('src')).content)
    except:
        pass          
  