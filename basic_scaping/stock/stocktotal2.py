from bs4 import BeautifulSoup
import requests
# 네이버 증권 기본 주소
basic = 'https://finance.naver.com'
# 특정 종목 주소 
item1 = 'https://finance.naver.com/item/main.nhn?code=093230'
def makesoup(url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(basic, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def majorInfo(urlItem):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(urlItem, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')
    info = []
    # 제목과 코드
    name = soup.find('div',{'class':'wrap_company'}).find('h2').text
    print(soup.find('div',{'class':'description'}).find('span',{'class':'code'}).text)
    # 크롤링 시작: 508 오늘 가격
    info += [soup.find('p',{'class':'no_today'}).find('span',{'class':'blind'}).text]
    # 전일대비 + 퍼센트 
    info += ([i.text for i in soup.find('p',{'class':'no_exday'}).find_all('span',{'class':'blind'})])
    info += ([i.find('span',{'class':'blind'}).text for i in soup.find_all('td',{'class':'first'})])
    # 테이블 안에 있는 내용(이 한줄로 거의 대부분 커버), 특정 테이블 지정한 다음 각 요소를 출력한 뒤, 각 출력 요소인 blind가 숨어있는 요소를 모두 출력 
    info += [i.find('span',{'class':'blind'}).text for i in soup.find('table',{'class':'no_info'}).find_all('td')]
    # 계산할 때를 대비하여 실수형으로 바꿔줌
    info = [float(i.replace(',','')) for i in info]
    info.insert(0, name)
    #주식명 저장하기 
    with open(r'C:\Users\ERC\Pictures\Saved Pictures\\'+name+'.jpg','wb') as f:
        f.write(requests.get(soup.find('img',{'id':'img_chart_area'}).get('src')).content)
    return info

total = []
j = 1
for j in range(5):
    try:
        id_name = '_topItems' + str(j)
        list_of_items = [basic + i.get('href') for i in makesoup(basic).find('tbody',{'id':id_name}).find_all('a')]
        for i in list_of_items:
            total.append(majorInfo(i))
    except:
        pass
    j +=1

import pandas as pd
df = pd.DataFrame(total, columns=['종목명',	'현재가' ,	'전일대비',	'비율',	'전일',	'시가',	'전일',	'고가',	'거래금액',	'시가',	'저가',	'거래대금'])
df.to_clipboard()