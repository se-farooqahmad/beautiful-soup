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
container = 'script:contains("@type")'
jersey_no_selector = '.sidearm-roster-player-jersey-number'
bio_selector = '.fullbio'
for sports in sports_data:
    rosters = sports['schedule_roster_news_links'][1]['url']
    sports_url = base_url.format(rosters)
    print("Sports' roster link")
    print(sports_url)
    response = requests.get(sports_url, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(response.text,"html.parser")
    players_data = json.loads(soup.select_one(container).get_text())['item']
    count = 0
    for players in players_data:
        name = players['name']
        link = players['url']
        image = players['image']['url']
        bio_res = requests.get(link , headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'})
        bio_soup = BeautifulSoup(bio_res.text,"html.parser")
        jersey_no = bio_soup.select_one(jersey_no_selector).get_text()
        bio = bio_soup.select_one(bio_selector).get_text()
        count = count + 1
        print('Player', count)
        player = {
            'Name' : name,
            'Jersey No.' : jersey_no.strip(),
            'Link' : link,
            'Image' : image,
            'Bio' : bio.strip()
        }
        print(player)
        print("")