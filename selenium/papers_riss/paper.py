from bs4 import BeautifulSoup
import requests


url = 'http://www.riss.or.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=%ED%8F%B4%ED%81%AC%EB%A3%A8%EA%B7%B8%EB%A8%BC&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=0&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&image_yn=&gubun=&kdc=&ttsUseYn=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=re_a_kor&colName=re_a_kor&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query=%EA%B0%95%EB%82%A8%EC%95%84%ED%8C%8C%ED%8A%B8'
soup = BeautifulSoup(requests.get(url).text, 'lxml')

with open(r'D:\user\Documents\git hub\fast_campus\selenium\a.txt','w',encoding ='utf8') as f:
    for j in soup.find_all('div',{'class':'srchResultListW'}):
        for i in j.find_all('p',{'class':'title'}):
            f.write(i.text)
            f.write(i.find('a').get('href'))
            f.write('\n')
