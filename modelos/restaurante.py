from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Restaurante".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avalicao = Avaliacao(cliente, nota)
            self._avaliacao.append(avalicao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qntd_avaliacoes = len(self._avaliacao)
        media = round(soma_notas/qntd_avaliacoes, 1)
        return media
    
    def adicionar_no_cardapio(self,item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)


    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio, start=1):
                if hasattr(item,'_descricao'):
                        mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Descrição: {item._descricao}'
                        print(mensagem_prato)
                else:
                        mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item._tamanho}'
                        print(mensagem_bebida)

