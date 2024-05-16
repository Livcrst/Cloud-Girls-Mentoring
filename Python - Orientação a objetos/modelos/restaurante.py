from modelos.avaliação import Avaliacao

class Restaurante: 
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False #usar _ indica que um atributo é privado
        Restaurante.restaurantes.append(self)
        self.__avaliacao__ = []
        self.cardapio = []
    # serve para mostrar o que tem no objeto como uma string
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    #
    @classmethod #indicam metodos exclusivos da classe.
    def listar_restaurantes(cls):
        for r in Restaurante.restaurantes:
            print(f'{r.nome} | {r.categoria} | {r._ativo}')
    #

    @property
    # usando property serve para modificar como um atributo vai ser exibido
    # def ativo(self):
    #     if self._ativo:
    #         return '☑'
    #     else:
    #         return '☒'
    #
    def alternar_estado(self):
        if self._ativo:
            self._ativo = False
            print(f'O restaurante {self.nome} foi desativado com sucesso!')
        else:
            self._ativo = True
            print(f'O restaurante {self.nome} foi ativado com sucesso!')
    @property
    def ativo(self):
        return '☑' if self._ativo else '☒'
    def receber_avaliacao(self, cliente, nota):
        Avaliacao = Avaliacao(cliente, nota)
        self.__avaliacao__.append(Avaliacao)
    #
    @property #O property serve tbm para indicar que cada objeto criado terá essa propriedade.
    def calcular_media(self):
        if not self.__avaliacao__:
            return 0
        else:
            soma = 0
            for avaliacao in self.__avaliacao__:
                soma += avaliacao.nota
            return soma / len(self.__avaliacao__)
    
    def adicionar_item_do_cardapio(self, item):
        self.cardapio.append(item)
        # print(f'A bebida {nome_bebida} foi adicionada com sucesso!')

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self.nome} \n')
        # for item in self.cardapio:
        #     print(item)
        # print('Fim do cardápio')

        for i, item in enumerate(self.cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i} - {item.nome} - R$ {item.preco:.2f} - {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i} - {item.nome} - R$ {item.preco:.2f}'
                print(mensagem_bebida)
            
