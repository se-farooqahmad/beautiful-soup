import requests
import time
from bs4 import BeautifulSoup

website_url = 'https://gamecocksonline.com/'
website_response = requests.get(website_url)
website_parsed_html = BeautifulSoup(website_response.content,"html.parser")

roster_links_css_selector ='[href*=roster]'

base_url = "https://gamecocksonline.com{}"

players_links_css_selectors = '.text-wrapper h3 a'


for rosters in website_parsed_html.select(roster_links_css_selector):
    partial_href_url = rosters.get('href')
    roster_url = base_url.format(partial_href_url)
    
    roster_reponse = requests.get(roster_url)
    roster_parsed_html = BeautifulSoup(roster_reponse.content,"html.parser")    
    
    for players in roster_parsed_html.select(players_links_css_selectors):
        players_href_url = players.get('href')
        players_response = requests.get(players_href_url)
        players_parsed_html = BeautifulSoup(players_response.content,"html.parser")
        name_css = '.container h1'
        img_css = '.bio__aside img'
        bio_css = '.bio__bio'
        name = players_parsed_html.select_one(name_css).get_text()
        image = players_parsed_html.select_one(img_css).get("src")
        #bio = players_parsed_html.select_one(bio_css).get_text()

        print(name)
        #time.sleep(1)
        
