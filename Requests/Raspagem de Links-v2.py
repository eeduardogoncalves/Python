"""
by Eduardo Gonçalves
Consulte - https://www.youtube.com/channel/UCYl0lZjwjafsQyGQ_6xfiKw?sub_confirmation=1
"""

import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.example.com')
soup = BeautifulSoup(page.content, 'html.parser')

# Find all links on the page
links = soup.find_all('a')

# Print the links
for link in links:
    print(link.get('href'))
