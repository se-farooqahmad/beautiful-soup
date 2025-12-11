import requests
import json
response = requests.get("https://iuhoosiers.com/services/adaptive_components.ashx?type=main-navigation&count=10&start=0&extra=%7B%7D")
data = json.loads(response.text)[0]['items']
base_url = 'https://iuhoosiers.com/{}'
for item in data:
    partial_url = item['schedule_roster_news_links'][1]['url']
    url = base_url.format(partial_url)
    
