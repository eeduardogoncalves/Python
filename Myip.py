import requests


url = requests.get("https://ipapi.co/json/")
r = url.json()

print("Meu ip : ",r['ip'])
print("Pais de origem : ",r["country_name"])
print("Cidade : ",r["city"])
print("Regiao: ",r["region"])
print("Code : ",r["region_code"])
print("Latitude: ",r["latitude"])
print("longitude: ",r["longitude"])
print("Operadora: ",r["org"])