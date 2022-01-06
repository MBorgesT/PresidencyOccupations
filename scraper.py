from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from bs4 import BeautifulSoup

from datetime import datetime
import pandas as pd

options = webdriver.FirefoxOptions()
options.add_argument('--width=1000')
options.add_argument('--height=800')
options.add_argument('--disable-logging') 
s = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(
    service=s, 
    options=options
)
driver.set_page_load_timeout(10)

day = datetime(2019, 1, 2)
rows = []
while day.year != 2022:
    year = day.year
    month = '%02d' % day.month
    day = '%02d' % day.day
    url = 'https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/' + \
        f'agenda-do-presidente-da-republica/{year}-{month}-{day}'
    try: # hack to bypass infinite page load, even though totally loaded
        driver.get(url)
    except Exception:
        pass

    bs = BeautifulSoup(driver.page_source, 'lxml')

    compromissos = bs.find('li', {'class': 'item-compromisso-wrapper'})
    print(f'len: {len(compromissos())}')

    input()
