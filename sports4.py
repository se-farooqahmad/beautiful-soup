import requests
import json
from bs4 import BeautifulSoup
import re

response = requests.get('https://uwbadgers.com/', headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'})
soup = BeautifulSoup(response.text,"html.parser")
print(response.status_code)
selector = 'script:contains("main-navigation")'
base_url = 'https://uwbadgers.com{}'

raw_data = re.findall('({.*})', soup.select_one(selector).get_text())[0]


for sport in json.loads(raw_data)['data'][0]['items']:
    if not sport['schedule_roster_news_links']:
        continue

    sport_partial_url = sport['schedule_roster_news_links'][1]['url']
    sports_url = base_url.format(sport_partial_url)

    print(sports_url)
