import requests
from bs4 import BeautifulSoup
import re

def clean(content):
    return re.sub('\s|\n', '', content)

response = requests.get("https://www.powerfood.ch/sortiment/protein-eiweiss/whey-protein/?order=topseller&p=2")
if response.status_code != 200:
    exit()
    
parsed_html = BeautifulSoup(response.content, "html.parser")

product_css = '.card-body'
name_css = '.product-name'
price_css = '.product-price'
stars_css = '.point-rating.point-full'
partial_star = '.point-rating.point-partial'

product_cards = parsed_html.select(product_css)

for card in product_cards:
    product_name = card.select_one(name_css).get_text()
    price = card.select_one(price_css).get_text()
    rating = len(card.select(stars_css))

    partial = card.select_one(partial_star)
    if partial:
        partial_style = card.select_one(partial_star).get('style')
        partial_rating = (100 - int(re.findall(r'(\d+%)', partial_style)[0].replace('%', '')))/100
        rating += partial_rating
    
    product = {
        'name': product_name.strip(),
        'price': clean(price),
        'rating': rating
    }
    
    
    print(product['name'])