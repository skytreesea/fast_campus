url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=&exQuery=&exQueryText=&order=&onHanja=&strSort=&p_year1=&p_year2=&iStartCount=0&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&image_yn=&gubun=&kdc=&ttsUseYn=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=re_a_kor&colName=re_a_kor&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query=%ED%83%80%EB%8B%B9%EC%84%B1+%EC%A1%B0%EC%82%AC'
basic = 'http://www.riss.kr'
from bs4 import BeautifulSoup
import requests
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = BeautifulSoup(requests.get(url, headers = headers).text,'lxml')
for i in soup.find_all('div',{'class':'cont'}):
    print(i.find('p',{'class':'title'}).text)
    print(i.find('p',{'class':'etc'}).text)
    detail = basic + i.find('p',{'class':'title'}).find('a').get('href')
    try:
        driver.get(detail)
        driver.find_elements_by_class_name('btnKakaoi')[0].click()
        print(driver.find_elements_by_class_name('innerArea')[0].text)
    except:
        pass