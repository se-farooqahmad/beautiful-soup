import requests
import time
from bs4 import BeautifulSoup

#fetching website's homepage
main_url = "https://mgoblue.com/sports/baseball/roster"
response = requests.get(main_url)
parsed_html = BeautifulSoup(response.content,"html.parser")

#generating the link to every player
base_url = "https://mgoblue.com{}"
#_s means selector / css selector
player_profile_links_s = '.s-person-card__content-call-to-action a'

#brings back the tag which matches the above selector
#brings back only a single tag because select_one is used 
#~next_player = parsed_html.select_one(player_profile_links_s) 
#getting the desired attribute of the respective tag
#~next_player = next_player.get("href")


#~next_url = base_url.format(next_player)

#fetching the tags using selector
#getting multiple tags because "select" is used which means select many/all
#traversing on all of the extracted tags one by one
for profile_tag in parsed_html.select(player_profile_links_s):
    partial_url = profile_tag.get("href")
    profile_link = base_url.format(partial_url)

    response = requests.get(profile_link)
    soup = BeautifulSoup(response.content,"html.parser")
    print(response.status_code)
    name_css = '.c-rosterbio__player__name span'
    image_css = '.c-rosterbio__player__image img'
    bio_css = '.legacy_to_nextgen'

    #fetching the name's tag using the css selector(name_css) via select_one
    #extracting the text i.e. the name from the specific tag using get_text()
    name = soup.select_one(name_css).get_text()
    image = soup.select_one(image_css).get("src")
    bio = soup.select_one(bio_css).get_text()

    print(name,image)
    time.sleep(2)