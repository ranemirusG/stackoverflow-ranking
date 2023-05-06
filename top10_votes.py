import requests
import json

url = f"https://api.stackexchange.com/2.3/questions?order=desc&sort=votes&site=stackoverflow"
response = requests.get(url)
data = json.loads(response.text)

with open('top10_votes.rst', 'w') as file:
    for i in range(10):
        question = data['items'][i]
        title = question['title']
        link = question['link']
        file.write(f"{i + 1}.\n")
        file.write(f"`{title} <{link}>`_\n\n")

