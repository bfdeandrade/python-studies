import requests

r = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")

question_data = r.json()['results']