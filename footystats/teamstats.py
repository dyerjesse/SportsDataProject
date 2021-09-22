import requests
import json


response = requests.get("https://api.football-data-api.com/league-matches?key=749c030e9b03727c95239d2eafaac41efafa185f35996ac07591bbbbc2f9e47d&season_id=6135")
data = response.json()

united = []
for row in data['data']:
	if row['status'] != 'incomplete':
		if row['home_name'] == "Manchester United" or row['away_name'] == "Manchester United":
			print(row)
			print('\n')
			united.append(row)

for row in united:
	print(row)
	print('\n')

total_home_xg = 0
total_away_xg = 0
for row in united:
	if row['home_name'] == "Manchester United":
		home_xg_perform = row['homeGoalCount'] - row['team_a_xg']
		print("For Manchester United's home game against ", row['away_name'], ", united overperformed their xg by ", home_xg_perform, " goals.")
		total_home_xg = total_home_xg + row['team_a_xg']
	if row['away_name'] == "Manchester United":
		away_xg_perform = row['awayGoalCount'] - row['team_b_xg']
		total_away_xg = total_away_xg + row['team_b_xg']
		print("For Manchester United's away game against ", row['home_name'], ", united overperformed their xg by ", away_xg_perform, " goals.")


print("United's home xg is ", total_home_xg)
print("United's away xg is ", total_away_xg)


total_xg = total_home_xg + total_away_xg

print("United's total xg is ", total_xg)

with open('new.json', 'w', encoding='utf-8') as team_data:
    json.dump(united, team_data, ensure_ascii=False, indent=4)