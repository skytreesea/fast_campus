from bs4 import BeautifulSoup 
import requests, re
basic = 'http://www.riss.kr/'
# 키워드만 바꿔가면서 넣으면 됨
query = '지방 공기업'
# 여러 키워드로 동시에 검색하여 논문정보
basic= 'http://www.riss.kr'
url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query=%EB%8F%84%EC%8B%9C%EC%9E%AC%EC%83%9D&queryText=&iStartCount=0&iGroupView=5&icate=all&colName=re_a_kor&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&pageScale=10&orderBy=&fsearchMethod=&isFDetailSearch=&sflag=1&searchQuery=%EB%8F%84%EC%8B%9C%EC%9E%AC%EC%83%9D&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&resultKeyword=&pageNumber=1&p_year1=&p_year2=&dorg_storage=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&language_code=&ccl_code=&language=&inside_outside=&fric_yn=&image_yn=&regnm=&gubun=&kdc=&ttsUseYn='
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = BeautifulSoup(requests.get(url, headers = headers).text, 'lxml')
urls = []
for i in soup.find_all('div',{'class':'cont'}):
    print([i.find('p',{'class':'title'}).find('a').text]+[j.text for j in i.find('p',{'class':'etc'}).find_all('span')])
    # for item in i.find('p',{'class':'title'}):
    #     try:
    #         print(item.find('a').text )
    #         urls.append(basic + item.find('a').get('href') )
    #     except:
    #         pass

# for i in soup.find_all('p',{'class':'etc'}):
#     try:
#         print([j.text for j in i.find_all('span')] )
#     except:
#         pass 