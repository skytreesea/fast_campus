from bs4 import BeautifulSoup 
import requests, re
basic = 'http://www.riss.kr/'

query = '금융지리'
url = ('http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query={}&queryText=&iStartCount=0&iGroupView=5&icate=all&colName=re_a_kor&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&pageScale=10&orderBy=&fsearchMethod=&isFDetailSearch=&sflag=1&searchQuery=%ED%96%89%EB%8F%99%EA%B2%BD%EC%A0%9C%ED%95%99&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&resultKeyword=&pageNumber=1&p_year1=&p_year2=&dorg_storage=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&language_code=&ccl_code=&language=&inside_outside=&fric_yn=&image_yn=&regnm=&gubun=&kdc=&ttsUseYn=').format(query)
# 봇으로 인식하지 않기 위해서는 다음과 같은 헤더를 달아줌
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')
info = []
info2 =[]
# 제목 크롤링 
for i in soup.find_all('p',{'class':'title'}):  
    # print([j.text for j in i.find_all('span')])
    try:
        info.append([i.find('a').text , basic + i.find('a').get('href') ])
    except:
        pass
# 논문 정보 크롤링
for i in soup.find_all('p',{'class':'etc'}):   
    info2.append([j.text for j in i.find_all('span')])
# 두 개 정보 합치기
for i in range(len(info)):
    info[info.index(info[i])] = info[i] + info2[i]
#판다스 데이터프레임 
import pandas as pd 
df = pd.DataFrame(info) 
df.to_clipboard()