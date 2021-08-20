import json

with open('matchday1.json', 'r') as f:
	data = json.load(f)

lst = []
for row in data:
	row['name'] = str(row['name'])
	row['team'] = str(row['team'])
	row['rank'] = int(row['rank'])
	row['goals'] = int(row['goals'])
	row['assists'] = int(row['assists'])
	row['goal_cont'] = row['goals'] + row['assists']
	row['perce_assist'] = row['assists']/row['goal_cont']*100
	row['perce_goals'] = row['goals']/row['goal_cont']*100
	lst.append(row)

for row in lst:
	print(row, '\n')

team_goals = 0
team_data = []
for row in lst:
	if row['team'] == 'Manchester United':
		team_goals = team_goals + row['goals']
		#team_data.append(team_goals)

print(team_data)

tg = 0
x = []
for row in lst:
	if row['team'] == "Manchester United":
		tg = tg+row['goals']
		print(tg)
		if row['team'] == '':
			x.append(tg)

print(x)




	