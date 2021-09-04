import json

with open('matchday3.json', 'r') as file:
	data = json.load(file)

'''
t_one = 0 #Arsenal
t_two = 0 #Aston Villa
t_three = 0 #Brentford FC
t_four = 0 #Brighton
t_five = 0 #Burnley
t_six = 0 #Chelsea
t_seven = 0 #Crystal Palace
t_eight = 0 #Everton
t_nine = 0 #Leeds United
t_ten = 0 #Leicester City
t_eleven = 0 #Liverpool
t_twelve = 0 #Manchester City
t_thirteen = 0 #Manchester United
t_fourteen = 0 #Newcastle United
t_fifteen = 0 #Norwich City
t_sixteen = 0 #Southampton
t_seventeen = 0 #Tottenham
t_eighteen = 0 #Watford
t_nineteen = 0 #West Ham United
t_twenty = 0 #Wolves

for row in data:
	row['goals'] = int(row['goals'])
	if row['team'] == 'Arsenal FC':
		t_one = t_one + row['goals']
	elif row['team'] == 'Aston Villa':
		t_two = t_two + row['goals']
	elif row['team'] == 'Brentford FC':
		t_three = t_three + row['goals']
	elif row['team'] == 'Brighton & Hove Albion':
		t_four = t_four + row['goals']
	elif row['team'] == 'Burnley FC':
		t_five = t_five + row['goals']
	elif row['team'] == 'Chelsea FC':
		t_six = t_six + row['goals']
	elif row['team'] == 'Crystal Palace':
		t_seven = t_seven + row['goals']
	elif row['team'] == 'Everton FC':
		t_eight = t_eight + row['goals']
	elif row['team'] == 'Leeds United':
		t_nine = t_nine + row['goals']
	elif row['team'] == 'Leicester City':
		t_ten = t_ten + row['goals']
	elif row['team'] == 'Liverpool FC':
		t_eleven = t_eleven + row['goals']
	elif row['team'] == 'Manchester City':
		t_twelve = t_twelve + row['goals']
	elif row['team'] == 'Manchester United':
		t_thirteen = t_thirteen + row['goals']
	elif row['team'] == 'Newcastle United':
		t_fourteen = t_fourteen + row['goals']
	elif row['team'] == 'Norwich City':
		t_fifteen = t_fifteen + row['goals']
	elif row['team'] == 'Southampton FC':
		t_sixteen = t_sixteen + row['goals']
	elif row['team'] == 'Tottenham Hotspur':
		t_seventeen = t_seventeen + row['goals']
	elif row['team'] == 'Watford FC':
		t_eighteen = t_eighteen + row['goals']
	elif row['team'] == 'West Ham United':
		t_nineteen = t_nineteen + row['goals']
	elif row['team'] == 'Wolverhampton Wanders':
		t_twenty = t_twenty + row['goals']

print(t_seven)

team_lst = []
for row in data:
	if row['team'] not in team_lst:
		team_lst.append(row['team'])

for team in team_lst:
	print(team)
'''


'''
tottenham -- Tottenham Hotspur
west ham -- West Ham United
manchester united -- Manchester United
chelsea -- Chelsea FC
liverpool -- Liverpool FC
everton -- Everton FC
manchester city -- Manchester City
brighton -- Brighton & Hove Albion
leicester city -- Leicester City
brentford -- Brentford FC
aston villa -- Aston Villa
watford -- Watford FC
southhampton -- Southampton FC
crystal palace -- Crystal Palace
leeds united -- Leeds United
burnley -- Burnley FC
newcastle -- Newcastle United
wolves -- Wolverhampton Wanderers
Norwich city -- Norwich City
Arsenal -- Arsenal FC
'''
#if row['team'] == 'Arsenal FC':

Arsenal = 0 #Arsenal
Aston = 0 #Aston Villa
Brentford = 0 #Brentford FC
Brighton = 0 #Brighton
Burnley = 0 #Burnley
Chelsea = 0 #Chelsea
Crystal = 0 #Crystal Palace
Everton = 0 #Everton
Leeds = 0 #Leeds United
Leicester = 0 #Leicester City
Liverpool = 0 #Liverpool
t_twelve = 0 #Manchester City
t_thirteen = 0 #Manchester United
Newcastle = 0 #Newcastle United
Norwich = 0 #Norwich City
Southampton = 0 #Southampton
Tottenham = 0 #Tottenham
Watford = 0 #Watford
West = 0 #West Ham United
Wolves = 0 #Wolves

for row in data:
	row['goals'] = int(row['goals'])
	if row['team'] == 'Arsenal FC':
		t_one = t_one + row['goals']
	elif row['team'] == 'Aston Villa':
		t_two = t_two + row['goals']
	elif row['team'] == 'Brentford FC':
		t_three = t_three + row['goals']
	elif row['team'] == 'Brighton & Hove Albion':
		t_four = t_four + row['goals']
	elif row['team'] == 'Burnley FC':
		t_five = t_five + row['goals']
	elif row['team'] == 'Chelsea FC':
		t_six = t_six + row['goals']
	elif row['team'] == 'Crystal Palace':
		t_seven = t_seven + row['goals']
	elif row['team'] == 'Everton FC':
		t_eight = t_eight + row['goals']
	elif row['team'] == 'Leeds United':
		t_nine = t_nine + row['goals']
	elif row['team'] == 'Leicester City':
		t_ten = t_ten + row['goals']
	elif row['team'] == 'Liverpool FC':
		t_eleven = t_eleven + row['goals']
	elif row['team'] == 'Manchester City':
		t_twelve = t_twelve + row['goals']
	elif row['team'] == 'Manchester United':
		t_thirteen = t_thirteen + row['goals']
	elif row['team'] == 'Newcastle United':
		t_fourteen = t_fourteen + row['goals']
	elif row['team'] == 'Norwich City':
		t_fifteen = t_fifteen + row['goals']
	elif row['team'] == 'Southampton FC':
		t_sixteen = t_sixteen + row['goals']
	elif row['team'] == 'Tottenham Hotspur':
		t_seventeen = t_seventeen + row['goals']
	elif row['team'] == 'Watford FC':
		t_eighteen = t_eighteen + row['goals']
	elif row['team'] == 'West Ham United':
		t_nineteen = t_nineteen + row['goals']
	elif row['team'] == 'Wolverhampton Wanders':
		t_twenty = t_twenty + row['goals']

print(t_seven)

team_lst = []
for row in data:
	if row['team'] not in team_lst:
		team_lst.append(row['team'])

for team in team_lst:
	if team is in data:
	print(team)

