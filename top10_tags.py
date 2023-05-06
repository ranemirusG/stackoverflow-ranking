import requests
import json
from collections import Counter

url = "https://api.stackexchange.com/2.3/questions?pagesize=100&order=desc&sort=votes&site=stackoverflow"
response = requests.get(url)
data = json.loads(response.text)

tags_counter = Counter()
for i in range(10):
    url = f"https://api.stackexchange.com/2.3/questions?pagesize=100&order=desc&sort=votes&site=stackoverflow&page={i+1}"
    response = requests.get(url)
    data = json.loads(response.text)
    for item in data['items']:
        tags = item['tags']
        tags_counter.update(tags)

top_tags = tags_counter.most_common(10)

table_rows = ""
for i, (tag, count) in enumerate(top_tags):
    table_rows += f"| {i+1}. | {tag} | {count} |\n"

table_header = "| Rank | Tag | Frequency |\n"
table_divider = "| ---- | --- | --------- |\n"

table = table_header + table_divider + table_rows

with open("top10_tags.rst", "w") as f:
    f.write(table)

