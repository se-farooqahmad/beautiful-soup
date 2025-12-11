import requests
import time
from bs4 import BeautifulSoup

website_url = 'https://arkansasrazorbacks.com/'
website_response = requests.get(website_url)
website_parsed_html = BeautifulSoup(website_response.text,"html.parser")

roster_links_css_selector =".sports [href*='/roster']:not([href*='#'])"

base_url = "https://arkansasrazorbacks.com/{}"
players_links_css_selectors = "td a[href*='/roster/']"


for rosters in website_parsed_html.select(roster_links_css_selector):
    partial_href_url = rosters.get('href')
    roster_url = base_url.format(partial_href_url)
    
    roster_reponse = requests.get(roster_url)
    roster_parsed_html = BeautifulSoup(roster_reponse.content,"html.parser")    
    
    for players in roster_parsed_html.select(players_links_css_selectors):
        players_href_url = players.get('href')
        players_response = requests.get(players_href_url)
        players_parsed_html = BeautifulSoup(players_response.content,"html.parser")
        name_css = '.bordeaux_bio__title h1'
        img_css = '.bordeaux_bio__profile_picture img'
        bio_css = '[itemprop=articleBody]'
        name = players_parsed_html.select_one(name_css).get_text()
        image = players_parsed_html.select_one(img_css).get("src")
        bio = players_parsed_html.select_one(bio_css).get_text()

        print(name,image)
        time.sleep(2)
        
