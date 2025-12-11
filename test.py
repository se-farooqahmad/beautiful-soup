import requests
from bs4 import BeautifulSoup
map = {'One':1,'Two':2, 'Three':3, 'Four':4, 'Five':5}

response = requests.get("https://books.toscrape.com/")
if response.status_code != 200:
    exit()
    
parsed_html = BeautifulSoup(response.content, "html.parser")

product_css = '.product_pod'
name_css = '.product_pod h3 a'
price_css = '.price_color'
stars_css = '.star-rating'
image_css = '.image_container img'
product_cards = parsed_html.select(product_css)
products = []

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
print(products)