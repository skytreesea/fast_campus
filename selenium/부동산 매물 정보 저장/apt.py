import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
basic = 'https://land.naver.com/'
driver = webdriver.Chrome(r'C:\Users\ERC\Documents\chromedriver.exe')
driver.get(basic)
box = driver.find_element_by_xpath('//*[@id="queryInputHeader"]')
box.send_keys('은마\n')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="ct"]/div[2]/div[1]/div[2]/div/div/div[1]/div/a/div[1]').click()
time.sleep(3)

title = [i.text for i in driver.find_elements_by_class_name('item_title')]
price = [i.text for i in driver.find_elements_by_class_name('price_line')]
total = [title, price]

driver.save_screenshot(r'C:\Users\ERC\Pictures\Saved Pictures\스크린샷\은마.png')
import pandas as pd
df= pd.DataFrame(total).transpose()
df.to_clipboard()