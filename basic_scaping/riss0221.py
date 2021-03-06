from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=%EB%B6%88%EC%95%88%EC%9E%A5%EC%95%A0&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=0&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&image_yn=&gubun=&kdc=&ttsUseYn=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=re_a_kor&colName=re_a_kor&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query=%EB%B6%88%EC%95%88%EC%9E%A5%EC%95%A0'
basic = 'http://www.riss.kr'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = BeautifulSoup(requests.get(url, headers = headers).text,'lxml')

url2 = basic + soup.find('div',{'class':'cont'}).find('p',{'class':'title'}).find('a').get('href')
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
soup = BeautifulSoup(requests.get(url, headers = headers).text,'lxml')

data =[]
abs=[]
# csv 형으로 집어넣기 
for i in soup.find_all('div',{'class':'cont'}):  
    data.append([i.find('p',{'class':'title'}).text, basic + i.find('p',{'class':'title'}).find('a').get('href') ])
    # 새로 가져온 부분
    try:
        driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\chromedriver.exe')
        new_url = basic + i.find('p',{'class':'title'}).find('a').get('href')
        driver.get(new_url)
        driver.find_element_by_xpath('//*[@id="soptionview"]/div/div[2]/div[1]/div/div[2]/p/a').click()
        abs.append(driver.find_element_by_id('abs2').text)
    except:
        pass
    
import pandas as pd 
df = pd.DataFrame(abs)
df.to_clipboard()
 
