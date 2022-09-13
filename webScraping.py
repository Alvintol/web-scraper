import requests
import functools
from bs4 import BeautifulSoup
from csv import writer

response = requests.get(
    'https://www.webscraper.io/test-sites/e-commerce/allinone')
soup = BeautifulSoup(response.text, 'html.parser')

items = soup.findAll(class_='col-sm-4 col-lg-4 col-md-4')

avgPriceList = []
avgRatingList = []
avgPrice = 0
avgRating = 0

with open('average.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Price', 'Rating']
    csv_writer.writerow(headers)

    for item in items:
        # print('-------ITEM-------:', '\n', item)

        price = item.find(class_='pull-right price').get_text()
        price = price.replace('$', '')

        avgPriceList.append(float(price))
        avgPrice = functools.reduce(
            lambda a, b: a+b, avgPriceList) / len(avgPriceList)

        print('-------PRICE-------:', '\n', price)

        # link = item.find('a')['href']
        # print('-------LINK-------:', '\n', link)

        rating = item.find(attrs={'data-rating': True})

        avgRatingList.append(len(rating))
        avgRating = float(functools.reduce(lambda a, b: a+b,
                          avgRatingList) / len(avgRatingList))

        csv_writer.writerow([avgPrice, avgRating])

        print('-------RATING-------:', '\n', len(rating))
print('-------AVERAGE PRICE-------:', '\n', f'${avgPrice:.2f}')
print('-------AVERAGE RATING-------:', '\n', f'{avgRating:.2f}')
