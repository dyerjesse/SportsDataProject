import requests

response = requests.get("https://api.football-data-api.com/test-call?key=749c030e9b03727c95239d2eafaac41efafa185f35996ac07591bbbbc2f9e47d")

for row in response.json():
	for items in row:
		print(items[0])