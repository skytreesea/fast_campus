import requests
from bs4 import BeautifulSoup
url = 'http://openAPI.ep.go.kr:8088/sample/xml/EpModelRestaurantDesignate/1/5/'
soup = BeautifulSoup(requests.get(url).text, 'lxml')
print(soup.find_all('row'))