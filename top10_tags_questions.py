import requests
import json
from collections import Counter

# Make API call to retrieve the 1000 most voted questions
url = "https://api.stackexchange.com/2.3/questions?pagesize=100&order=desc&sort=votes&site=stackoverflow"
response = requests.get(url)
data = json.loads(response.text)

# Count the occurrence of each tag and store the most voted question for each tag
tags_counter = Counter()
questions_by_tag = {}
for i in range(10):
    url = f"https://api.stackexchange.com/2.3/questions?pagesize=100&order=desc&sort=votes&site=stackoverflow&page={i+1}"
    response = requests.get(url)
    data = json.loads(response.text)
    for item in data['items']:
        tags = item['tags']
        for tag in tags:
            tags_counter[tag] += 1
            if tag not in questions_by_tag:
                questions_by_tag[tag] = {'title': item['title'], 'link': item['link']}
                break

# Sort the tags by count and generate a numbered list of the most voted question for each tag
top_tags = tags_counter.most_common(10)
numbered_list = ""
for i, (tag, count) in enumerate(top_tags):
    question_title = questions_by_tag[tag]['title'].replace('|', '-')
    question_link = questions_by_tag[tag]['link']
    numbered_list += f"{i + 1}.\n`{question_title} <{question_link}>`_\n\n"

# Output the result to a file
with open('top10_tags_questions.rst', 'w') as file:
    file.write(numbered_list)

