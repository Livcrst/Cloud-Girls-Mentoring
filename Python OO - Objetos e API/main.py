from fastapi import FastAPI, Query
import requests

app = FastAPI()

# Esse decorator serve para indicar que quero disponibilzar alguma coisa
@app.get("/api/hello") #Definindo a minha rota a ser utilizada
def hello_wolrd(): #Função que é acessada para a rota (endpoint)
    return {"Hello": "World"}

@app.get("/api/restaurante")
def ola(restaurante: str = Query(None)): #Não pesquisar nada por padrão
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    # GET retorna dados
    # print(response)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados':dados_json}
        # print(dados_json)
        dados_restaurante = []
        for item in dados_json:
            if item ['Company'] == restaurante: 
            # if nome_do_restaurante not in dados_restaurante:
                dados_restaurante = []
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description'],
                    
                })
                return {'Restaurante':dados_restaurante, 'Cardapio':dados_restaurante}
    else:
        print(f'Ocorreu um erro {response.status_code}')