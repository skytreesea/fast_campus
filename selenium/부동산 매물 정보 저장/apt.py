import requests,re
from bs4 import BeautifulSoup
f = open(r'C:\Users\ERC\Documents\GitHub\fast_campus\api\apt_test.xml','r',encoding='utf8')
data = f.read()
f.close()
soup = BeautifulSoup(data,'lxml') 
print([re.sub('\\n','',i) for i in re.split('[가-힣].+?\>', soup.item.text)])
# total = []
# total.append([i.text for i in soup.find_all('일')])

# import pandas as pd 
# df = pd.DataFrame(total).transpose()
# df.to_clipboard()
# print(df)