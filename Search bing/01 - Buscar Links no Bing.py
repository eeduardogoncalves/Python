

import requests

# Substitua pela sua chave de API
api_key = "API_KEY"

# A consulta que você deseja enviar à API
query = "XXX"

# Montando a url com a consulta e a chave
url = f"https://api.bing.microsoft.com/v7.0/search?q={query}"
headers = {"Ocp-Apim-Subscription-Key": api_key}

# Enviando a requisição para a API
response = requests.get(url, headers=headers)

# Verificando se a requisição foi bem sucedida
if response.status_code == 200:
    # Carregando os dados retornados pela API em um dicionario
    data = response.json()
    # iterando sobre os resultados da busca
    for item in data['webPages']['value']:
        # Exibindo as urls encontradas
        print(item['url'])
else:
    # Exibindo o codigo de status da resposta
    print("Erro:", response.status_code)
