import requests
import json


response = requests.get("https://api.football-data-api.com/league-players?key=749c030e9b03727c95239d2eafaac41efafa185f35996ac07591bbbbc2f9e47d&season_id=6135")
data = response.json()

count = 0 
for row in data['data']:
	count += 1
	print(count)
	print(row)

lst = []
for row in data['data']:
	