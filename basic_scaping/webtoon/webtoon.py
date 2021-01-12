# image_url = 'https://ssl.pstatic.net/imgfinance/chart/item/area/day/195990.png?sidcode=1608439379118'
#image_url으로부터 content 얻음
# img_data = requests.get(image_url).content
# os.chdir(r'####경로를 정확히 입력 #####')
# #content 저장함
# with open('image_name.jpg', 'wb') as handler:
#     handler.write(img_data)

from bs4 import BeautifulSoup as bs
import requests,re
url = ('https://comic.naver.com/webtoon/weekday.nhn')
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get(url, headers = headers)
soup = bs(res.text, 'lxml')
# ol만 찾아서 text를 찾을 경우0
# for i in soup.find_all('ol', {'id':'realTimeRankUpdate'}):
#     print(i.text)
for i in soup.find_all('ol', {'id':'realTimeRankFavorite'}):
    print([j.get('title') for j in i.find_all('a')])
for i in soup.find_all('div', {'class':'thumb6'}):
    print(i.find('a').get('title'))