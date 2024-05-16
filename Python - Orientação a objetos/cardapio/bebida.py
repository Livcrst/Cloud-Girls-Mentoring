from cardapio import item_cardapio

class Bebida:
    def __init__(self, nome, preco, tamanho):
        # self.nome = nome
        # self.preco = preco
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        return f'{self.nome} - R$ {self.preco:.2f}'
    
    def aplicar_descricao(self):
        self._preco -= (self._preco*0.05)