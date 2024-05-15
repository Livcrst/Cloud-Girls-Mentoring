from modelos.restaurante import Restaurante

# pycache é um arquivo que o python usa para interpretar os objetos criados

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()
    
    
    
restaurante = Restaurante("praça","gourmet")
restaurante = Restaurante("shark","sushi")
restaurante = Restaurante("burrito","mexicano")


restaurante.nome = 'Praça'
restaurante.categoria = 'Gourmet'

# usar vars em um objeto gera um dicionario com os atributos com os atributos salvos de um dicionario.