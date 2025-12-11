import requests 
import csv
from bs4 import BeautifulSoup
map = {'One':1,'Two':2, 'Three':3, 'Four':4, 'Five':5}

url = 'https://books.toscrape.com/'
response = requests.get(url)
base_url = 'https://books.toscrape.com/catalogue/{}'

soup = BeautifulSoup(response.content,"html.parser")

product_css = '.product_pod'
name_css = '.product_pod h3 a'
price_css = '.price_color'
stars_css = '.star-rating'
image_css = '.image_container img'

product_cards = soup.select(product_css)

products = []
next_page = '.next a'
count = 0
while 1:
    print(count)
    for card in product_cards:
        product_name = card.select_one(name_css).get('title')
        price = card.select_one(price_css).get_text()
        rating = card.select_one(stars_css).get('class')[-1]
        image = card.select_one(image_css).get('src')

        products.append({
            'name': product_name.strip(),
            'price': (price),
            'rating': map[rating],
            'img' : (image)
        })

    next_page_url = soup.select_one(next_page)
    if not next_page_url: #or appended_url=='https://books.toscrape.com/catalogue/page-50.html':
        break

    next_page_url = next_page_url.get("href")
    if 'catalogue/' in next_page_url:
        next_page_url = next_page_url.replace('catalogue/','')
    appended_url = base_url.format(next_page_url)


    response = requests.get(appended_url)
    soup = BeautifulSoup(response.content,"html.parser")
    product_cards = soup.select(product_css)
    count += 1 

file = open('./books.csv','w')
writer = csv.DictWriter(file, list(products[0].keys()))
writer.writeheader()

for product in products:
    writer.writerow(product)
