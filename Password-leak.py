import requests
pastebin = requests.get("https://pastebin.com/cq5Gvkyk")
resposta = pastebin.text
while True:
    i = input("digite seu email : ") in resposta
    print(i)

# Este codigo vai buscar no pastebin senhas vazadas
