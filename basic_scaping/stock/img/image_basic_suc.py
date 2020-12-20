import requests, os
image_url = 'https://ssl.pstatic.net/imgfinance/chart/item/area/day/195990.png?sidcode=1608439379118'
#image_url으로부터 content 얻음
img_data = requests.get(image_url).content
os.chdir(r'C:\Users\ERC\Documents\GitHub\fast_campus\basic_scaping\stock')
#content 저장함
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)