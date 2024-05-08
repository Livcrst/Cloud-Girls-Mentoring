# Import que limpa o console
import os
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                      {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True}]


def exibir_menu():
    print('Hello Wolrd, Sabor express')
    # Mostrar informações
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante ')
    print('4. Sair')


# import this -- The Zen of the python

#Definição de funções
def finalizar_app():
    os.system('cls')
    print('Encerrando aplicação')
    print('')
#
def opcao_invalida():
    print('Opção inválida /n')
    print('Digite uma opção válida! Tente novamente')
#
def cadastrar_restaurante():
    os.system('cls') #Essa chaamda serve para limpar o terminal 
    print('Cadastrar restaurante \n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    input ('Digite uma tecla para voltar ao menu principal.')
    main()
#
def listar_restaurante():
    os.system('cls') #Essa chaamda serve para limpar o terminal 
    print('Lista de restaurantes cadastrados \n')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        print(f'.{nome}')
    print('\n')
    input ('Digite uma tecla para voltar ao menu principal.')
    main()
#
def alternar_status_restaurante():
    print('Alternando o status de restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            if restaurante['ativo'] == True:
                restaurante['ativo'] = False
                print(f'O restaurante {nome_restaurante} foi desativado com sucesso!')
            else:
                restaurante['ativo'] = True
                print(f'O restaurante {nome_restaurante} foi ativado com sucesso!')
        continue
# Tem como definir o arquivo principal do python, definindo uma função chamada __main__
def main():
    exibir_menu()
def escolher_opcoes():
        # Pedir informações
    opc = int(input('Escolha uma opção: '))
    # print(f'A opção que vc escolheu foi {opc}')
    try:
        if opc == 1:
            # print('Cadastrar restaurante')
            cadastrar_restaurante()
        elif opc == 2:
            # print('Listar restaurantes')
            listar_restaurante()

        elif opc == 3:
            alternar_status_restaurante()
        elif opc == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

if __name__ == '__main__':
    main()
    escolher_opcoes()