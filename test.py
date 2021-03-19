import requests
import pprint
import json
from bs4 import BeautifulSoup
a = requests.get('https://stats.modxvm.com/ru/stats/players/42472522').text

soup = BeautifulSoup(a, "html.parser")

print (soup.find_all("div", {"class": "h2"})[2].text)