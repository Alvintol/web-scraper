import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.webscraper.io/test-sites/e-commerce/allinone')
soup = BeautifulSoup(response.text, 'html.parser')

items = soup.findAll(class_='col-sm-4 col-lg-4 col-md-4')

for item in items:
  print('-------ITEM-----:', '\n', item)