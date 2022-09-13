import requests
import functools
from bs4 import BeautifulSoup
from csv import writer

response = requests.get(
    'https://www.webscraper.io/test-sites/e-commerce/allinone')
soup = BeautifulSoup(response.text, 'html.parser')

items = soup.findAll(class_='col-sm-4 col-lg-4 col-md-4')

avgPrice = []
avgRating = []

for item in items:
    # print('-------ITEM-------:', '\n', item)

    price = item.find(class_='pull-right price').get_text()
    avgPrice.append(price)
    print('-------PRICE-------:', '\n', price)
    print('-------AVERAGE PRICE-------:', '\n', avgPrice)

    # link = item.find('a')['href']
    # print('-------LINK-------:', '\n', link)

    rating = item.find(attrs={'data-rating': True})
    avgRating.append(len(rating))
    reducedRating = functools.reduce(lambda a, b: a+b, avgRating) / len(avgRating)
    print('-------RATING-------:', '\n', len(rating))
    print('-------AVERAGE RATING-------:', '\n', f'{reducedRating:.2f}')
