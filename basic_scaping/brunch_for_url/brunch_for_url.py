# url 읽기 실습 브런치 글 연속 크롤링하기 
# 특정 브런치의 글 연속으로 크롤링하기 
import requests, re
from bs4 import BeautifulSoup 
url = ('https://brunch.co.kr/@skytreesea/')
# 봇으로 인식하지 않기 위해서는 다음과 같은 헤더를 달아줌


# 링크 타고 들어가서 제목과 본문을 같이 크롤링 하는데 성공
def scrape_lines(url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    soup  = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')
    for i in soup.find_all('p', {'class':'wrap_item item_type_text'}):
        print(i.text)

for i in range(100,106):
    scrape_lines(url + str(i))