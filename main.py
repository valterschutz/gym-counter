from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://api.rscount.se/rs/counter/000B91906EDA')

results = []
content = browser.page_source
soup = BeautifulSoup(content, features='lxml')

sleep(5)

# print(soup.find(id='odometer').get_text())

while True:
    results = browser.find_elements_by_xpath('//*[@id="odometer"]')
    result = results[0].text
    newresult = int(result.replace('\n', ''))
    print(newresult, type(newresult))
    sleep(5)
