import requests
from bs4 import BeautifulSoup
response = requests.get("https://quotes.toscrape.com/")

if response.status_code != 200:
    exit()

parseHTML = BeautifulSoup(response.content, "html.parser")

quotes_css = '.quote'
text_css = '.quote span'
quotations = parseHTML.select(quotes_css)

quotes = []

for quote in quotations:
    text = quote.select_one(text_css).get_text()
    quotes.append({
        'Quote' : (text)
    })
print(quotes)