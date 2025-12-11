import requests
import json
from bs4 import BeautifulSoup
import re

response = requests.get('https://baylorbears.com/', headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'})
soup = BeautifulSoup(response.text,"html.parser")
print(response.status_code)

selector = 'script:contains("main-navigation")'
base_url = 'https://baylorbears.com{}'

raw_data = re.findall('({.*})', soup.select_one(selector).get_text())[0]

data = json.loads(raw_data)
men_sports = data['data'][0]['items']
women_sports = data['data'][1]['items']

sports_data = men_sports + women_sports

roster = '/roster'



for sports in sports_data:
    sport_partial_url = sports['url']
    sports_url = base_url.format(sport_partial_url)
    sports_url = sports_url + roster
    print(sports_url)

response = requests.get('https://baylorbears.com/sports/baseball/roster/', headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'})
soup = BeautifulSoup(response.text,"html.parser")
print(response.status_code)

container = 'script:contains("slugify")'

players_raw_data = re.findall('{"id.*}', soup.select_one(container).get_text())[0]

players_data = json.loads(players_raw_data)['players']
dash = "-"
slash = "/"
initial_url = "https://baylorbears.com/sports/baseball/roster/"
for players in players_data:
    first_name = players['first_name']
    last_name = players['last_name']
    id = players['rp_id']
    id = str(id)
    players_url = initial_url+first_name+dash+last_name+slash+id
    print(players_url)
