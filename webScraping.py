import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.webscraper.io/test-sites/e-commerce/allinone')
soup = BeautifulSoup(response.text, 'html.parser')