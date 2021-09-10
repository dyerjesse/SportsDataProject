import requests

response = requests.get("https://api.football-data-api.com/league-matches?key=749c030e9b03727c95239d2eafaac41efafa185f35996ac07591bbbbc2f9e47d&season_id=1625")

print(response.json())