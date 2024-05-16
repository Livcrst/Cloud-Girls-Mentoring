from cardapio import ItemCardapio

class Prato:
    def __init__(self, nome, preco, descricao):
        super().__init__(self, nome, preco, descricao) #Isso indica que quero usar a superclasse para criar (conceito de herança)
        self.descricao = descricao
    #
    def __str__(self):
        return f'{self.nome} - R$ {self.preco:.2f}'
    def aplicar_desconto(self):
        self.preco -= (self.preco*0.08)