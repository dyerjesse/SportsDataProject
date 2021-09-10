import json

with open('matchday3.json', 'r') as md3:
	data_md3 = json.load(md3)

arsenal = [] #Arsenal
aston = [] #Aston Villa
brentford = [] #Brentford FC
brighton = [] #Brighton
burnley = [] #Burnley
chelsea = [] #Chelsea
crystal = [] #Crystal Palace
everton = [] #Everton
leeds = [] #Leeds United
leicester = [] #Leicester City
liverpool = [] #Liverpool
city = [] #Manchester City
united = [] #Manchester United
newcastle = [] #Newcastle United
norwich = [] #Norwich City
southampton = [] #Southampton
tottenham = [] #Tottenham
watford = [] #Watford
westham = [] #West Ham United
wolves = [] #Wolves

for row in data_md3:
	if row['team'] == "Arsenal FC":
		arsenal.append(row)
	if row['team'] == "Aston Villa":
		aston.append(row)
	if row['team'] == "Brentford FC":
		brentford.append(row)
	if row['team'] == "Brighton & Hove Albion":
		brighton.append(row)
	if row['team'] == "Burnley FC":
		burnley.append(row)
	if row['team'] == "Chelsea FC":
		chelsea.append(row)
	if row['team'] == "Crystal Palace":
		crystal.append(row)
	if row['team'] == "Everton FC":
		everton.append(row)
	if row['team'] == "Leeds United":
		leeds.append(row)
	if row['team'] == "Leicester City":
		leicester.append(row)
	if row['team'] == "Liverpool FC":
		liverpool.append(row)
	if row['team'] == "Manchester City":
		city.append(row)
	if row['team'] == "Manchester United":
		united.append(row)
	if row['team'] == "Newcastle United":
		newcastle.append(row)
	if row['team'] == "Norwich City":
		norwich.append(row)
	if row['team'] == "Southampton FC":
		southampton.append(row)
	if row['team'] == "Tottenham Hotspur":
		tottenham.append(row)
	if row['team'] == "Watford FC":
		watford.append(row)
	if row['team'] == "West Ham United":
		westham.append(row)
	if row['team'] == "Wolverhampton Wanders":
		wolves.append(row)

'''
team_goals = 0
team_assists = 0
for row in data_md3:
	if row['team'] in data_md3 == "Manchester United":
		row['rank'] = int(row['rank'])
		row['goals'] = int(row['goals'])
		row['assists'] = int(row['assists'])
		row['goal_cont'] = row['goals'] + row['assists']
		if row['team'] == "Manchester United":
			team_goals = team_goals + row['goals']
			team_assists = team_assists + row['assists']
'''

for row in data_md3:
	row['rank'] = int(row['rank'])
	row['goals'] = int(row['goals'])
	row['assists'] = int(row['assists'])
	row['goal_cont'] = row['goals'] + row['assists']

#Arsenal team stats
arsenal_goals = 0
arsenal_assists = 0
for row in united:
	arsenal_goals = arsenal_goals + row['goals']
	arsenal_assists = arsenal_assists + row['assists']
for row in arsenal:
	row['total_goals'] = arsenal_goals
	row['total_assists'] = arsenal_assists
	row['goal_percentage'] = row['goals']/arsenal_goals*100
	row['assist_percentage'] = row['assists']/arsenal_assists*100
for row in arsenal:
	print(row)

#Aston Villa team stats
#aston_rank = 0
aston_goals = 0
aston_assists = 0
for row in united:
	aston_goals = aston_goals + row['goals']
	aston_assists = aston_assists + row['assists']
	#aston_rank = aston_rank + 1
	#row['team_rank'] = aston_rank
for row in aston:
	row['total_goals'] = aston_goals
	row['total_assists'] = aston_assists
	row['goal_percentage'] = row['goals']/aston_goals*100
	row['assist_percentage'] = row['assists']/aston_assists*100
for row in aston:
	print(row)

print('\n')
#Manchester United team stats
united_rank = 0
united_goals = 0
united_assists = 0
for row in united:
	united_goals = united_goals + row['goals']
	united_assists = united_assists + row['assists']
	united_rank = united_rank + 1
	row['team_rank'] = united_rank
for row in united:
	row['total_goals'] = united_goals
	row['total_assists'] = united_assists
	row['goal_percentage'] = row['goals']/united_goals*100
	row['assist_percentage'] = row['assists']/united_assists*100
for row in united:
	print(row)

'''
for row in arsenal:
	print(row)
print('\n')
for row in aston:
	print(row)
print('\n')
for row in brentford:
	print(row)
print('\n')
for row in brighton:
	print(row)
print('\n')
for row in burnley:
	print(row)
print('\n')
for row in chelsea:
	print(row)
print('\n')
for row in crystal:
	print(row)
print('\n')
for row in everton:
	print(row)
print('\n')
for row in leeds:
	print(row)
print('\n')
for row in leicester:
	print(row)
print('\n')
for row in liverpool:
	print(row)
print('\n')
for row in city:
	print(row)
print('\n')
for row in united:
	print(row)
	print('\n')
print('\n')
for row in newcastle:
	print(row)
print('\n')
for row in norwich:
	print(row)
print('\n')
for row in southampton:
	print(row)
print('\n')
for row in tottenham:
	print(row)
print('\n')
for row in watford:
	print(row)
print('\n')
for row in westham:
	print(row)
print('\n')
for row in wolves:
	print(row)
'''