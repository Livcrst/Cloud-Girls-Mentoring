import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
# GET retorna dados
print(response)

if response.status_code == 200:
    dados_json = response.json()
    # print(dados_json)
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item ['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        dados_restaurante[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description'],
            
        })
else:
    print(f'Ocorreu um erro {response.status_code}')

#percorrer todos os restaurante e pegar todos os items
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4) #criar o arquivo pelo json
# Esse código serve para criar arquivos json com os itens dos restaurantes
            