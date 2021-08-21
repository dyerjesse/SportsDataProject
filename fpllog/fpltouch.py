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

'''
for row in lst:
	print(row, '\n')
'''

select = input('Type in a team name: ')
team_goals = 0
for row in lst:
	if row['team'] == select:
		team_goals = team_goals + row['goals']

print(select, " scored a total of ", team_goals, " this game week.")

team_lst = []
for row in data:
	if row['team'] == select:
		team_lst.append(row)
		perc_goals = row['goals']/team_goals*100
		team_lst.append(perc_goals)

for items in team_lst:
	print(items)
'''
total_team = 0
perc_goals = 0
#select = input('Type in a team name: ')
for row in data:
	if row['team'] == select:
		total_team = total_team + row['goals']
		if row['goals'] != 0:
			perc_goals = row['goals']/total_team*100
		print(row, total_team, perc_goals, '\n')

'''


	