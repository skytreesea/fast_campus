from bs4 import BeautifulSoup 
import requests, re, time
basic = 'http://www.riss.kr'
# 키워드만 바꿔가면서 넣으면 됨
from selenium import webdriver
#키를 입력하기 위해서 필요한 모듈
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\chromedriver.exe')
def make_total(query):
    total=[]
    for i in range(1,5):
        # 봇으로 인식하지 않기 위해서는 다음과 같은 헤더를 달아
        url = ('http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery={}&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount={}&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&image_yn=&gubun=&kdc=&ttsUseYn=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=re_a_kor&colName=re_a_kor&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query={}').format(query,str(i*10),query) #어떤 부분을 바꿔야 페이지가 바뀌는지 확인하는 작업 필요 
        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
        soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')
        for item in soup.find_all('div',{'class':'cont'}):
            total.append(
            [i.text for i in item.find('p',{'class':'title'}).find_all('a')]+
            [basic + i.get('href') for i in item.find('p',{'class':'title'}).find_all('a')]+
            [i.text for i in item.find('p',{'class':'etc'}).find_all('a')])
    return total

final = make_total('')
for i in final:
    driver.get(i[1])
    driver.find_elements_by_class_name('btnKakaoi')[0].click()
    i.insert(2,driver.find_elements_by_class_name('innerArea')[0].text)
    time.sleep(1)
import pandas as pd
df = pd.DataFrame(final)
df.to_clipboard()
# 한번에 제목과 url 저장
# total  = [[i.find('a').text, basic + i.find('a').get('href')] for i in soup.find_all('p',{'class':'title'}) if i.find('a')]
