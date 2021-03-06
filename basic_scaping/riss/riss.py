from bs4 import BeautifulSoup 
import requests, re
basic = 'http://www.riss.kr/'
# 키워드만 바꿔가면서 넣으면 됨
query = '지방 공기업'
# 여러 키워드로 동시에 검색하여 논문정보 저장할 수 있도록 함
keywords = ['지방공기업','지방공단','타당성검토']
info = []
info2 =[]

def risscollector(keyword):
# 봇으로 인식하지 않기 위해서는 다음과 같은 헤더를 달아줌
    for i in range(1,20): # 200개까지 논문 찾기
        url = ('http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery={}&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount={}&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&image_yn=&gubun=&kdc=&ttsUseYn=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=re_a_kor&colName=re_a_kor&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query={}').format(keyword,str(i*10),keyword) #어떤 부분을 바꿔야 페이지가 바뀌는지 확인하는 작업 필요 

        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
        soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')

        # 제목 크롤링 
        for i in soup.find_all('p',{'class':'title'}):  
            try:
                info.append([i.find('a').text , basic + i.find('a').get('href') ])
            except:
                pass
        # 논문 정보 크롤링
        for i in soup.find_all('p',{'class':'etc'}):   
            info2.append([j.text for j in i.find_all('span')][:5])
        # 두 개 정보 인위적으로 합치기: csv형 만듦
        for i in range(len(info)):
            info[info.index(info[i])] = info[i] + info2[i]
    return info
total = []
for i in keywords:
    total = total + risscollector(i)

#판다스 데이터프레임 100개까지 붙이기 
import pandas as pd 
df = pd.DataFrame(info) 
df.to_clipboard()