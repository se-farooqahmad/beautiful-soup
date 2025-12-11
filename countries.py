import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.scrapethissite.com/pages/simple/")
if response.status_code != 200:
    exit()
    
parsed_html = BeautifulSoup(response.content, "html.parser")

product_css = '.country'
name_css = '.country-name'
capital_css = '.country-capital'
population_css ='.country-population'
area_css = '.country-area'
product_cards = parsed_html.select(product_css)
products = []

for card in product_cards:
    
    country = card.select_one(name_css).get_text()
    capital = card.select_one(capital_css).get_text()
    population = card.select_one(population_css).get_text()
    area = card.select_one(area_css).get_text()
    print(country, capital, population, area)
 
