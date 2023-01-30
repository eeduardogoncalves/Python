import requests
from bs4 import BeautifulSoup

keyword = "example"

google_search = "https://www.google.com/search?q=" + keyword

response = requests.get(google_search)
soup = BeautifulSoup(response.text, "html.parser")

results = soup.find_all("div", class_="r")

for result in results[:100]:
    title = result.find("h3").text
    print(title)
