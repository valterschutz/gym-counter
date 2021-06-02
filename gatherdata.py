from datetime import datetime
from time import sleep
import pandas as pd
from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=False, size=(800,600))
display.start()

# options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
# browser = webdriver.Firefox(options=options)

options = webdriver.ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)


browser.get('http://api.rscount.se/rs/counter/000B91906EDA')


sleep(30)  # Allow page to load

# Main loop, run for several days and make new data file for each day
while True:
    oldresult = 9000  # First reading may be incorrect

    # Gather data until new day
    while True:
        results = browser.find_elements_by_xpath('//*[@id="odometer"]')
        result = int(results[0].text.replace('\n', ''))
        if result > oldresult + 50:  # Most likely an error
            sleep(1)
            continue
        timestr, weekdaystr = datetime.now().strftime('%H:%M %A').split()
        datestr = str(datetime.today().date())
        print(timestr, weekdaystr, result)
        f = open(f'data/{datestr}.csv', 'a')
        f.write(f"{timestr},{weekdaystr},{result}\n")
        f.close()
        oldresult = result
        sleep(60)

