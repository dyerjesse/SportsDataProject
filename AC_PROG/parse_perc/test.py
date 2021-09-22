import json

with open('matchday4.json', 'r') as md3:
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

for row in data_md3:
	row['rank'] = int(row['rank'])
	row['goals'] = int(row['goals'])
	row['assists'] = int(row['assists'])
	row['goal_cont'] = row['goals'] + row['assists']

#Arsenal team stats
arsenal_rank = 0
arsenal_goals = 0
arsenal_assists = 0
for row in arsenal:
	arsenal_goals = arsenal_goals + row['goals']
	arsenal_assists = arsenal_assists + row['assists']
	arsenal_rank = arsenal_rank + 1
	row['team_rank'] = arsenal_rank
for row in arsenal:
	row['total_goals'] = arsenal_goals
	row['total_assists'] = arsenal_assists
	row['goal_percentage'] = row['goals']/arsenal_goals*100
	row['assist_percentage'] = row['assists']/arsenal_assists*100
for row in arsenal:
	print(row)

print('\n')

#Aston Villa team stats
aston_rank = 0
aston_goals = 0
aston_assists = 0
for row in aston:
	aston_goals = aston_goals + row['goals']
	aston_assists = aston_assists + row['assists']
	aston_rank = aston_rank + 1
	row['team_rank'] = aston_rank
for row in aston:
	row['total_goals'] = aston_goals
	row['total_assists'] = aston_assists
	row['goal_percentage'] = row['goals']/aston_goals*100
	row['assist_percentage'] = row['assists']/aston_assists*100
for row in aston:
	print(row)

print('\n')
#Brentford FC team stats
brentford_rank = 0
brentford_goals = 0
brentford_assists = 0
for row in brentford:
	brentford_goals = brentford_goals + row['goals']
	brentford_assists = brentford_assists + row['assists']
	brentford_rank = brentford_rank + 1
	row['team_rank'] = brentford_rank
for row in brentford:
	row['total_goals'] = brentford_goals
	row['total_assists'] = brentford_assists
	row['goal_percentage'] = row['goals']/brentford_goals*100
	row['assist_percentage'] = row['assists']/brentford_assists*100
for row in brentford:
	print(row)

print('\n')

#Brighton FC team stats
brighton_rank = 0
brighton_goals = 0
brighton_assists = 0
for row in brighton:
	brighton_goals = brighton_goals + row['goals']
	brighton_assists = brighton_assists + row['assists']
	brighton_rank = brighton_rank + 1
	row['team_rank'] = brighton_rank
for row in brighton:
	row['total_goals'] = brighton_goals
	row['total_assists'] = brighton_assists
	row['goal_percentage'] = row['goals']/brighton_goals*100
	row['assist_percentage'] = row['assists']/brighton_assists*100
for row in brighton:
	print(row)

print('\n')

#Burnley FC team stats
burnley_rank = 0
burnley_goals = 0
burnley_assists = 0
for row in burnley:
	burnley_goals = burnley_goals + row['goals']
	burnley_assists = burnley_assists + row['assists']
	burnley_rank = burnley_rank + 1
	row['team_rank'] = burnley_rank
for row in burnley:
	row['total_goals'] = burnley_goals
	row['total_assists'] = burnley_assists
	row['goal_percentage'] = row['goals']/burnley_goals*100
	row['assist_percentage'] = row['assists']/burnley_assists*100
for row in burnley:
	print(row)

print('\n')

#Chelsea FC team stats
chelsea_rank = 0
chelsea_goals = 0
chelsea_assists = 0
for row in chelsea:
	chelsea_goals = chelsea_goals + row['goals']
	chelsea_assists = chelsea_assists + row['assists']
	chelsea_rank = chelsea_rank + 1
	row['team_rank'] = chelsea_rank
for row in chelsea:
	row['total_goals'] = chelsea_goals
	row['total_assists'] = chelsea_assists
	row['goal_percentage'] = row['goals']/chelsea_goals*100
	row['assist_percentage'] = row['assists']/chelsea_assists*100
for row in chelsea:
	print(row)

print('\n')

#Crystal Palace team stats
crystal_rank = 0
crystal_goals = 0
crystal_assists = 0
for row in crystal:
	crystal_goals = crystal_goals + row['goals']
	crystal_assists = crystal_assists + row['assists']
	crystal_rank = crystal_rank + 1
	row['team_rank'] = crystal_rank
for row in crystal:
	row['total_goals'] = crystal_goals
	row['total_assists'] = crystal_assists
	row['goal_percentage'] = row['goals']/crystal_goals*100
	row['assist_percentage'] = row['assists']/crystal_assists*100
for row in crystal:
	print(row)

print('\n')

#Everton team stats
everton_rank = 0
everton_goals = 0
everton_assists = 0
for row in everton:
	everton_goals = everton_goals + row['goals']
	everton_assists = everton_assists + row['assists']
	everton_rank = everton_rank + 1
	row['team_rank'] = everton_rank
for row in everton:
	row['total_goals'] = everton_goals
	row['total_assists'] = everton_assists
	row['goal_percentage'] = row['goals']/everton_goals*100
	row['assist_percentage'] = row['assists']/everton_assists*100
for row in everton:
	print(row)

print('\n')

#Leeds team stats
leeds_rank = 0
leeds_goals = 0
leeds_assists = 0
for row in leeds:
	leeds_goals = leeds_goals + row['goals']
	leeds_assists = leeds_assists + row['assists']
	leeds_rank = leeds_rank + 1
	row['team_rank'] = leeds_rank
for row in leeds:
	row['total_goals'] = leeds_goals
	row['total_assists'] = leeds_assists
	row['goal_percentage'] = row['goals']/leeds_goals*100
	row['assist_percentage'] = row['assists']/leeds_assists*100
for row in leeds:
	print(row)

print('\n')

#Leicester City team stats
leicester_rank = 0
leicester_goals = 0
leicester_assists = 0
for row in leicester:
	leicester_goals = leicester_goals + row['goals']
	leicester_assists = leicester_assists + row['assists']
	leicester_rank = leicester_rank + 1
	row['team_rank'] = leicester_rank
for row in leicester:
	row['total_goals'] = leicester_goals
	row['total_assists'] = leicester_assists
	row['goal_percentage'] = row['goals']/leicester_goals*100
	row['assist_percentage'] = row['assists']/leicester_assists*100
for row in leicester:
	print(row)

print('\n')

#Liverpool FC team stats
liverpool_rank = 0
liverpool_goals = 0
liverpool_assists = 0
for row in liverpool:
	liverpool_goals = liverpool_goals + row['goals']
	liverpool_assists = liverpool_assists + row['assists']
	liverpool_rank = liverpool_rank + 1
	row['team_rank'] = liverpool_rank
for row in liverpool:
	row['total_goals'] = liverpool_goals
	row['total_assists'] = liverpool_assists
	row['goal_percentage'] = row['goals']/liverpool_goals*100
	row['assist_percentage'] = row['assists']/liverpool_assists*100
for row in liverpool:
	print(row)

print('\n')

#Manchester City FC team stats
city_rank = 0
city_goals = 0
city_assists = 0
for row in city:
	city_goals = city_goals + row['goals']
	city_assists = city_assists + row['assists']
	city_rank = city_rank + 1
	row['team_rank'] = city_rank
for row in city:
	row['total_goals'] = city_goals
	row['total_assists'] = city_assists
	row['goal_percentage'] = row['goals']/city_goals*100
	row['assist_percentage'] = row['assists']/city_assists*100
for row in city:
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

print('\n')

#Newcastle United team stats
newcastle_rank = 0
newcastle_goals = 0
newcastle_assists = 0
for row in newcastle:
	newcastle_goals = newcastle_goals + row['goals']
	newcastle_assists = newcastle_assists + row['assists']
	newcastle_rank = newcastle_rank + 1
	row['team_rank'] = newcastle_rank
for row in newcastle:
	row['total_goals'] = newcastle_goals
	row['total_assists'] = newcastle_assists
	row['goal_percentage'] = row['goals']/newcastle_goals*100
	row['assist_percentage'] = row['assists']/newcastle_assists*100
for row in newcastle:
	print(row)

print('\n')

#Norwich City team stats
norwich_rank = 0
norwich_goals = 0
norwich_assists = 0
for row in norwich:
	norwich_goals = norwich_goals + row['goals']
	norwich_assists = norwich_assists + row['assists']
	norwich_rank = norwich_rank + 1
	row['team_rank'] = norwich_rank
for row in norwich:
	row['total_goals'] = norwich_goals
	row['total_assists'] = norwich_assists
	row['goal_percentage'] = row['goals']/norwich_goals*100
	#row['assist_percentage'] = row['assists']/norwich_assists*100
for row in norwich:
	print(row)

print('\n')

#Southampton team stats
southampton_rank = 0
southampton_goals = 0
southampton_assists = 0
for row in southampton:
	southampton_goals = southampton_goals + row['goals']
	southampton_assists = southampton_assists + row['assists']
	southampton_rank = southampton_rank + 1
	row['team_rank'] = southampton_rank
for row in southampton:
	row['total_goals'] = southampton_goals
	row['total_assists'] = southampton_assists
	row['goal_percentage'] = row['goals']/southampton_goals*100
	row['assist_percentage'] = row['assists']/southampton_assists*100
for row in southampton:
	print(row)

print('\n')

#Tottenham team stats
tottenham_rank = 0
tottenham_goals = 0
tottenham_assists = 0
for row in tottenham:
	tottenham_goals = tottenham_goals + row['goals']
	tottenham_assists = tottenham_assists + row['assists']
	tottenham_rank = tottenham_rank + 1
	row['team_rank'] = tottenham_rank
for row in tottenham:
	row['total_goals'] = tottenham_goals
	row['total_assists'] = tottenham_assists
	row['goal_percentage'] = row['goals']/tottenham_goals*100
	row['assist_percentage'] = row['assists']/tottenham_assists*100
for row in tottenham:
	print(row)

print('\n')

#Watford FC team stats
watford_rank = 0
watford_goals = 0
watford_assists = 0
for row in watford:
	watford_goals = watford_goals + row['goals']
	watford_assists = watford_assists + row['assists']
	watford_rank = watford_rank + 1
	row['team_rank'] = watford_rank
for row in watford:
	row['total_goals'] = watford_goals
	row['total_assists'] = watford_assists
	row['goal_percentage'] = row['goals']/watford_goals*100
	row['assist_percentage'] = row['assists']/watford_assists*100
for row in watford:
	print(row)

print('\n')

#West Ham FC team stats
westham_rank = 0
westham_goals = 0
westham_assists = 0
for row in westham:
	westham_goals = westham_goals + row['goals']
	westham_assists = westham_assists + row['assists']
	westham_rank = westham_rank + 1
	row['team_rank'] = westham_rank
for row in westham:
	row['total_goals'] = westham_goals
	row['total_assists'] = westham_assists
	row['goal_percentage'] = row['goals']/westham_goals*100
	row['assist_percentage'] = row['assists']/westham_assists*100
for row in westham:
	print(row)

print('\n')

#Wolverhampton Wanderers FC team stats
wolves_rank = 0
wolves_goals = 0
wolves_assists = 0
for row in wolves:
	wolves_goals = wolves_goals + row['goals']
	wolves_assists = wolves_assists + row['assists']
	wolves_rank = wolves_rank + 1
	row['team_rank'] = wolves_rank
for row in wolves:
	row['total_goals'] = wolves_goals
	row['total_assists'] = wolves_assists
	row['goal_percentage'] = row['goals']/wolves_goals*100
	row['assist_percentage'] = row['assists']/wolves_assists*100
for row in wolves:
	print(row)

#Write team data to json
with open('arsenal.json', 'w', encoding='utf-8') as team_data:
    json.dump(arsenal, team_data, ensure_ascii=False, indent=4)

with open('astonvilla.json', 'w', encoding='utf-8') as team_data:
    json.dump(aston, team_data, ensure_ascii=False, indent=4)

with open('brentford.json', 'w', encoding='utf-8') as team_data:
    json.dump(brentford, team_data, ensure_ascii=False, indent=4)

with open('brighton.json', 'w', encoding='utf-8') as team_data:
    json.dump(brighton, team_data, ensure_ascii=False, indent=4)

with open('burnley.json', 'w', encoding='utf-8') as team_data:
    json.dump(burnley, team_data, ensure_ascii=False, indent=4)

with open('chelsea.json', 'w', encoding='utf-8') as team_data:
    json.dump(chelsea, team_data, ensure_ascii=False, indent=4)

with open('crystalpalace.json', 'w', encoding='utf-8') as team_data:
    json.dump(crystal, team_data, ensure_ascii=False, indent=4)

with open('everton.json', 'w', encoding='utf-8') as team_data:
    json.dump(everton, team_data, ensure_ascii=False, indent=4)

with open('leeds.json', 'w', encoding='utf-8') as team_data:
    json.dump(leeds, team_data, ensure_ascii=False, indent=4)

with open('leicester.json', 'w', encoding='utf-8') as team_data:
    json.dump(leicester, team_data, ensure_ascii=False, indent=4)

with open('liverpool.json', 'w', encoding='utf-8') as team_data:
    json.dump(liverpool, team_data, ensure_ascii=False, indent=4)

with open('manchestercity.json', 'w', encoding='utf-8') as team_data:
    json.dump(city, team_data, ensure_ascii=False, indent=4)

with open('manchesterunited.json', 'w', encoding='utf-8') as team_data:
    json.dump(united, team_data, ensure_ascii=False, indent=4)

with open('newcastle.json', 'w', encoding='utf-8') as team_data:
    json.dump(newcastle, team_data, ensure_ascii=False, indent=4)

with open('norwich.json', 'w', encoding='utf-8') as team_data:
    json.dump(norwich, team_data, ensure_ascii=False, indent=4)

with open('southampton.json', 'w', encoding='utf-8') as team_data:
    json.dump(southampton, team_data, ensure_ascii=False, indent=4)

with open('tottenham.json', 'w', encoding='utf-8') as team_data:
    json.dump(tottenham, team_data, ensure_ascii=False, indent=4)

with open('watford.json', 'w', encoding='utf-8') as team_data:
    json.dump(watford, team_data, ensure_ascii=False, indent=4)

with open('westham.json', 'w', encoding='utf-8') as team_data:
    json.dump(westham, team_data, ensure_ascii=False, indent=4)

with open('wolves.json', 'w', encoding='utf-8') as team_data:
    json.dump(wolves, team_data, ensure_ascii=False, indent=4)  

count = 0
for row in data_md3:
	count += 1

print("Outputting data for ", count, " players.")

print("Writing team data to json...")