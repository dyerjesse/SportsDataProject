import requests
import json


response = requests.get("https://api.football-data-api.com/league-players?key=749c030e9b03727c95239d2eafaac41efafa185f35996ac07591bbbbc2f9e47d&season_id=6135")
data = response.json()
'''
united = []
for row in data['data']:
	if row['club_team_id'] == 149:
		united.append(row)
		print(row)
		print('\n')
		#print(row['full_name'], ' Goals: ', row['goals_overall'], ' Assists: ', row['assists_overall'])

for items in united:
	print(items)
'''
a = input("Pick player A: ")
b = input("Pick player B: ")

player_a = []
player_b = []
for row in data['data']:
	if row['last_name'] == a:
		print(row['full_name'])
		print("Minutes Played: ", row['minutes_played_overall'])
		player_a.append(row['minutes_played_overall'])
		print("Goals Scored: ", row['goals_overall'])
		print("Assists: ", row['assists_overall'])
		print('\n')

for row in data['data']:
	if row['last_name'] == b:
		print(row)

print(player_a)