import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'C:\Users\ERC\Documents\파이썬\chromedriver.exe')
doit = 'http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791163031734#review'
driver.get(doit)
driver.find_element_by_id('review').click() 