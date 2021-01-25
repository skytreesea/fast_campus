# 클리앙 인기글 스크래핑 제목 성공
import requests, re, time, csv, os
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
os.chdir(r'C:\Users\ERC\Documents\GitHub\fast_campus\basic_scaping\clien')
#한글로 저장 안되는 문제 해결해야 
def writecsv(filename, the_list):
    #브라보 utf-8-sig: 대단한 발견
    with open(filename,'w', newline='', encoding='utf-8-sig') as f:
        a=csv.writer(f, delimiter=',')
        a.writerows(the_list)
def opencsv(filename):
    f=open(filename, 'r', encoding='utf-8-sig')
    reader=csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    return output

total = opencsv('clien_py_suc_ver2.0.csv')
total_new=[]
for url in total:
    posting = ''
    try: 
        soup = bs(requests.get(url[1]).text, 'html.parser')
        for i in soup.find_all('div', {'class':'post_article'}):
            posting += re.sub('\n\n','',i.text)
        url.append(posting)
    except: 
        pass
    if re.search('[가-힣]',url[0]):
        total_new.append(url)

writecsv('clien_with_posting_remove_duplicate.csv',total_new)
    

