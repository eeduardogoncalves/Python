"""
by Eduardo Gonçalves
Consulte - https://www.youtube.com/channel/UCYl0lZjwjafsQyGQ_6xfiKw?sub_confirmation=1
"""


import requests

api_key = "API_KEY"
cx = "CX"
q = "SEARCH"

url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={q}"

response = requests.get(url)
data = response.json()

if "items" in data:
    for item in data["items"]:
        link = item["link"]
        print(link)
else:
    print("No results found.")
