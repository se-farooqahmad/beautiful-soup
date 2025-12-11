import requests
import time
from bs4 import BeautifulSoup

website_url = 'https://scarletknights.com/'
website_response = requests.get(website_url)
website_parsed_html = BeautifulSoup(website_response.text,"html.parser")

roster_links_css_selector = '.roster'
players_links_css_selectors = '.sidearm-roster-player-name'

base_url = 'https://scarletknights.com{}'

for rosters in website_parsed_html.select(roster_links_css_selector):
    partial_href_url = rosters.get('href')
    roster_url = base_url.format(partial_href_url)

    roster_reponse = requests.get(roster_url)
    roster_parsed_html = BeautifulSoup(roster_reponse.content,"html.parser") 

    for players in roster_parsed_html.select(players_links_css_selectors):
        players_href_url = players.get('href')
        players_url = base_url.format(players_href_url)
        players_response = requests.get(players_url)
        players_parsed_html = BeautifulSoup(players_response.content,"html.parser")
        
        name_css = '.sidearm-roster-player-name '
        number_css = '.sidearm-roster-player-jersey-number'
        img_css = '.sidearm-roster-player-image '

        name = players_parsed_html.select_one(name_css).get_text()
        number = players_parsed_html.select_one(bio_css).get_text()
        image = players_parsed_html.select_one(img_css).get("src")

        print(name,image)
        time.sleep(2)
        