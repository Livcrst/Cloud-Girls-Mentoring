from abc import ABC, abstractmethod #Para criar moldes para classes implementarem

class ItemCardapio:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass
        