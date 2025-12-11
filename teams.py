import requests
import csv
from bs4 import BeautifulSoup

base_url_t = 'https://www.scrapethissite.com{}'
rows_css = '.team'
next_page_css = '[aria-label="Next"]'

teams = []
response = requests.get("https://www.scrapethissite.com/pages/forms/")
soup = BeautifulSoup(response.content, "html.parser")
while 1:
    next_page = soup.select_one(next_page_css)
    if not next_page:
        break
    next_page = next_page.get("href")
    next_page_url = base_url_t.format(next_page)
    response = requests.get(next_page_url)
    soup = BeautifulSoup(response.content, "html.parser")

    for row in soup.select(rows_css):
        name = row.select_one('.name').get_text().strip()
        year = row.select_one('.year').get_text().strip()
        wins = row.select_one('.wins').get_text().strip()
        losses = row.select_one('.losses').get_text().strip()


        team = {
            "name": name,
            "year": year,
            "wins": wins,
            "losses": losses,
        }
        teams.append(team)
    count += 1

writing_file = open('./teams.csv', 'w')
writer = csv.DictWriter(writing_file, list(teams[0].keys()))
writer.writeheader()

for team in teams:
    writer.writerow(team)