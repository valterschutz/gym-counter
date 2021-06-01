from datetime import datetime
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import matplotlib.pyplot as plt

browser = webdriver.Firefox()
browser.get('http://api.rscount.se/rs/counter/000B91906EDA')

sleep(5)

f = open('data.csv', 'a')

oldresult = 0  # First reading may be incorrect
for i in range(60):
    results = browser.find_elements_by_xpath('//*[@id="odometer"]')
    result = int(results[0].text.replace('\n', ''))
    if result > oldresult + 20:  # Most likely an error, try again
        sleep(2)
        continue
    nowtime = datetime.now()
    datestr, timestr = nowtime.strftime('%Y-%m-%d %H:%M').split()
    print(datestr, timestr, result)
    f.write(f"{datestr},{timestr},{result}\n")
    oldresult = result
    sleep(60)

f.close()
