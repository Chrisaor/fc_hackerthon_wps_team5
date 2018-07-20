import os

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/jihye/Downloads/chromedriver')
driver.implicitly_wait(3)

driver.get('https://www.skyscanner.co.kr/')

file_path = 'data/flight.html'
url = 'https://www.skyscanner.co.kr/transport/flights/nyca/sela/180719/180725/?'

if os.path.exists(url):
    html = open('file_path', 'rt').read
else:
    response = requests.get(url)
    html = response.text
    open(file_path, 'wt').write(html)

soup = BeautifulSoup(html, 'lxml')
table = soup.select_one('table.fqs-opts')
print(table)
