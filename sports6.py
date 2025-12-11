import requests
import json
from bs4 import BeautifulSoup
import re
base_url = "https://vucommodores.com{}"
response = requests.get("https://vucommodores.com")
parsed = BeautifulSoup(response.text, 'html.parser')
rosters_selector = "a[href*='/roster/']"
players_selector = "td a[href*='/roster/']:not([span])"
name_css = ".info .title h1"
image_css = ".player_bio img"
bio_css = ".player_bio__article"
for rosters in parsed.select(rosters_selector):
    partial_url = rosters.get('href')
    url = base_url.format(partial_url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for players in soup.select(players_selector):
        players_partial_url = players.get('href')
        players_url = base_url.format(players_partial_url)
        response = requests.get(players_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.select_one(name_css).get_text()
        name = name.replace(" ","")
        image = soup.select_one(image_css).get('src')
        bio = soup.select_one(bio_css).get_text()
        player = {
            'Name' : name.strip(),
            'Image' : image,
            'Bio' : bio.strip()
        }
        print(player)
        print("")
        
