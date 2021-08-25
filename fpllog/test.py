import json

with open('matchday2.json', 'r') as f:
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
		
for row in md1:
	if row['team'] == select:
		if team_goals != 0:
			row['perce_goals'] = row['goals']/team_goals*100
		if team_assists != 0:
			row['perce_assist'] = row['assists']/team_assists*100

for row in md1:
	if row['team'] == select:
		print(row)

print('\n')


lst = []
gcount = 0
for row in md1:
	while row['team'] not in lst:
		team = row['team']
		lst.append(team)
		break


print(lst)
print('\n')
print(team, gcount)
