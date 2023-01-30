"""
by Eduardo Gonçalves
Consulte - https://www.youtube.com/channel/UCYl0lZjwjafsQyGQ_6xfiKw?sub_confirmation=1
"""

import requests 
response = requests.get("https://www.example.com") 
print("status code", response.status_code) 
print("cabeçalho", response.headers) 
print("conteudo", response.content) 