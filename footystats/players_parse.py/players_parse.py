import requests
import json


response = requests.get("https://api.football-data-api.com/league-players?key=749c030e9b03727c95239d2eafaac41efafa185f35996ac07591bbbbc2f9e47d&season_id=6135")
data = response.json()


lst = []
for row in data['data']:
			lst.append(row)

for items in lst:
	del items['id']
	del items['competition_id']
	del items['first_name']
	del items['last_name']
	del items['known_as']
	del items['shorthand']
	del items['league']
	del items['league_type']
	del items['starting_year']
	del items['ending_year']
	del items['url']
	del items['club_team_2_id']
	del items['national_team_id']
	del items['birthday']
	del items['continent']
	del items['last_match_timestamp']

print(lst)

with open('playerstats.json', 'w', encoding='utf-8') as player_data:
    json.dump(lst, player_data, ensure_ascii=False, indent=4)
    print("Writing file to playerstats.json...")