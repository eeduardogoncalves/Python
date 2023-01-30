import requests
import re

# Substitua pela sua chave de API
key = ""

# A URL da página que você deseja pesquisar
url = ""

# Envia a solicitação à API da Bing
response = requests.get(f"https://api.bing.microsoft.com/v7.0/search?q={url}", headers={"Ocp-Apim-Subscription-Key": key})

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Carrega o conteúdo da página em um objeto JSON
    data = response.json()
    # Procurar por padrões de e-mail na página retornada
    email_pattern = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    pages = data.get('webPages', {})
    if 'value' in pages:
        for page in pages['value']:
            email = re.findall(email_pattern, page['snippet'])
            if email:
                print(email)
    else:
        print("Nenhum endereço de e-mail encontrado.")
else:
    # Exibe o código de status da resposta
    print(f"Erro: {response.status_code}")
