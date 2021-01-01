#반복문 적용 안 한 기본함수: 주식차트 이미지 크롤링
import requests, os
image_url = 'https://ssl.pstatic.net/imgfinance/chart/item/area/day/195990.png?sidcode=1608439379118'
#image_url으로부터 content 얻음
img_data = requests.get(image_url).content
os.chdir(r'D:\user\Documents\git hub\fast_campus\basic_scaping\stock\img')
#content 저장함
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)
