# 뷰티풀수프 상용어구
from bs4 import BeautifulSoup  
import requests 
import pandas as pd 
#네이버 기사 url만 바꾸기: 따옴표 안에 url을 붙여넣으세요.
productName = input('검색하고 싶은 키워드 입력하세요. 출력 결과는 엑셀에서 Ctrl-V로 붙여넣기 할 수 있습니다.')
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
basic = 'https://www.coupang.com'
url = 'https://www.coupang.com/np/search?component=&q={}&channel=user&page='.format(productName)
urls = []
# 각 상품정보에서 특정 정보를 리스트 형태로 모으기(데이터프레임 용)
def coupangData(soup):
    info=[] 
    for i in soup.find_all('li',{'class':'search-product'}):
        try:
            k=[i.find('div',{'class':'name'}).text,
            i.find('strong',{'class':'price-value'}).text,
            i.find('span',{'class':'star'}).text,
            i.find('span',{'class':'rating-total-count'}).text[1:-1],
            basic + i.find('a').get('href')]
            if i.find('span',{'class':'badge rocket'}):
                k.append('로켓')
            else:
                k.append('n/a')
            info.append(k)
        except:
            pass 
    return info

for i in range(1,5):
    try:
        urls.append(url+str(i))
    except:
        pass

info=[]
for i in [BeautifulSoup(requests.get(url, headers = headers).text, 'lxml') for url in urls]:
    try:
        info = info + coupangData(i)
    except:
        pass

# 판다스 이용해 자료를 행열 전환하고, 바로 df로 만들어 클립보드에 저장, 칼럼명 처음에 지정해주기 
df = pd.DataFrame(info, columns=['상품명','가격','리뷰평점','리뷰수','링크','로켓'])
# # 천의 자리 제거(가격)
df['가격']=df['가격'].str.replace(',', '').astype('int64')
# # 가격 높은 순으로 클립보드 저장
df.sort_values(by = '리뷰평점', ascending = False).to_clipboard()