from bs4 import BeautifulSoup
from selenium import webdriver
import requests

# driver = webdriver.Chrome(r'D:\user\Documents\git hub\fast_campus\selenium\chromedriver.exe')

# driver.implicitly_wait(3)
# driver.get('https://madangs.com/')
url = 'http://www.riss.or.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query=%EA%B2%BD%EC%A0%9C%EC%A7%80%EB%A6%AC%ED%95%99&queryText=&iStartCount=0&iGroupView=5&icate=all&colName=re_a_kor&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&pageScale=10&orderBy=&fsearchMethod=&isFDetailSearch=&sflag=1&searchQuery=%EA%B2%BD%EC%A0%9C%EC%A7%80%EB%A6%AC%ED%95%99&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&resultKeyword=&pageNumber=1&p_year1=&p_year2=&dorg_storage=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&language_code=&ccl_code=&language=&inside_outside=&fric_yn=&image_yn=&regnm=&gubun=&kdc=&ttsUseYn='
soup = BeautifulSoup(requests.get(url).text, 'lxml')

with open(r'D:\user\Documents\git hub\fast_campus\selenium\a.txt','w',encoding ='utf8') as f:
    for i in soup.find_all('p',{'class':'title'}):
        f.write(i.text)
        f.write('\n')
