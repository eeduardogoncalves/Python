"""
by Eduardo Gonçalves
Consulte - https://www.youtube.com/channel/UCYl0lZjwjafsQyGQ_6xfiKw?sub_confirmation=1
"""

import requests

api_key = "API_KEY"
cx = "CX"

results_per_page = 10
start = 1

while True:
    q = input("Enter a search query: ") 
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={q}&start={start}"
    response = requests.get(url)
    data = response.json()

    if "items" in data:
        for item in data["items"]:
            link = item["link"]
            print(link)
        start += results_per_page
    else:
        break
