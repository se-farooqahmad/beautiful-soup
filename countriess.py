import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

country_name_elements = soup.find_all('h3', class_='country-name')
country_capital_elements = soup.find_all('span', class_='country-capital')
country_pop_elements = soup.find_all('span', class_='country-population')
country_area_elements = soup.find_all('span', class_='country-area')

for element in country_name_elements:
    country_name = element.get_text(strip=True)
    country_cap = element.get_text(strip=True)
    country_pop = element.get_text(strip=True)
    country_area = element.get_text(strip=True)
    print(country_name)
