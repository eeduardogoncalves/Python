import requests
import json
import re

subscription_key = ""
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

emails = []

for result in results:
    # get the page content
    page_content = requests.get(result["url"]).text
    # extract email addresses using regular expression
    emails.extend(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", page_content))

# remove duplicates
emails = list(set(emails))

if emails:
    print("Emails found:")
    for email in emails:
        print(email)
else:
    print("No emails found.")
