import requests
import json

subscription_key = "API_KEY_AZURE"
search_url = "https://api.bing.microsoft.com/v7.0/search"

headers = {"Ocp-Apim-Subscription-Key" : subscription_key}

# get user input
user_input = input("Enter a keyword: ")

params  = {"q": user_input, "textDecorations":True, "textFormat":"HTML", "count":100}

response = requests.get(search_url, headers=headers, params=params)

if response.status_code != 200:
    print("Error code:", response.status_code)
    print("Error message:", response.json()["error"]["message"])
    exit()

if not response.json()['webPages']:
    print("No results found")
    exit()

results = response.json()["webPages"]["value"]

for result in results:
    link = result["url"]
    print(link)
