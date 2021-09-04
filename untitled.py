import json

with open('test-footystats.json', 'r') as file:
	data = json.load(file)

for row in data:
	print(row['data'])
