import requests
import json

tag = input("Enter the tag to search for: ")

# Make request to Stack Exchange API to get the most voted question with the given tag
url = f"https://api.stackexchange.com/2.3/questions?order=desc&sort=votes&tagged={tag}&site=stackoverflow"
response = requests.get(url)
data = json.loads(response.text)
question = data['items'][0]

# Get the title and link of the question
title = question['title']
link = question['link']

# Print the title and link of the question
print(f"Title: {title}")
print(f"Link: {link}")

