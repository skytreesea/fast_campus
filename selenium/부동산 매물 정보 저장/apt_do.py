import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\chromedriver.exe')
driver.get('https://land.naver.com/')
apt ='은마'
driver.find_element_by_xpath('//*[@id="queryInputHeader"]').send_keys(apt)
driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[1]/div/fieldset/a[1]').click()
#아파트로 들어가는 데까지는 성공
time.sleep(3)
driver.find_element_by_xpath('//*[@id="ct"]/div[2]/div[1]/div[2]/div/div/div[1]/div/a').click()
time.sleep(3)
driver.save_screenshot(r'C:\Users\ERC\Pictures\Saved Pictures\스크린샷\\'+ apt + '.png')

title =  [i.text for i in driver.find_elements_by_class_name('item_title')]
price = [i.text for i in driver.find_elements_by_class_name('price_line')]
new = [title, price]

import pandas as pd 
df = pd.DataFrame(new).transpose() 
df.to_clipboard() 