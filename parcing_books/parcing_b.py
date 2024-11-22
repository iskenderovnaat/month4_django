from django.test import TestCase

# Create your tests here.
import requests
from bs4 import BeautifulSoup as BS4

URL = 'http://books.toscrape.com'
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}


def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def get_data(html):
    bs = BS4(html, features='html.parser')
    items = bs.find_all('article', class_='product_pod')
    books_list = []
    for item in items:
        title = item.h3.a['title']
        image = URL + '/' + item.find('img')['src'].replace('../../', '')
        price = item.find('p', class_='price_color').text
        price = price.replace('Â£','')
        rating = item.find('p') ['class'][1]
        books_list.append({
            'title': title,
            'image': image,
            'price': price,
            'rating': rating
        })
    return books_list

def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        books_list = []
        for page in range(1, 2):
            response = get_html(URL + '/catalogue/page-' + str(page) + '.html')
            books_list.extend(get_data(response.text))
        return books_list
    else:
        raise Exception('Error Parsing Books to Scrape')


print(parsing())