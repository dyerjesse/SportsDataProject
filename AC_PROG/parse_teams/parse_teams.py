import json

with open('matchday3.json', 'r') as f:
	md1 = json.load(f)

select = input('Type in a team name: ')
team_goals = 0
team_assists = 0
for row in md1:
	row['rank'] = int(row['rank'])
	row['goals'] = int(row['goals'])
	row['assists'] = int(row['assists'])
	row['goal_cont'] = row['goals'] + row['assists']
	if row['team'] == select:
		team_goals = team_goals + row['goals']
		team_assists = team_assists + row['assists']

count = 0		
for row in md1:
	if row['team'] == select:
		if team_goals != 0:
			row['perce_goals'] = row['goals']/team_goals*100
		if team_assists != 0:
			row['perce_assist'] = row['assists']/team_assists*100
		count = count + 1
		row['team_rank'] = count
		row['total_team_goals'] = team_goals
		row['total_team_assists'] = team_assists

out = []
for row in md1:
	if row['team'] == select:
		out.append(row)

with open('newTeam.json', 'w', encoding='utf-8') as team_data:
    json.dump(out, team_data, ensure_ascii=False, indent=4)
    print("Writing file to newTeam.json...")

