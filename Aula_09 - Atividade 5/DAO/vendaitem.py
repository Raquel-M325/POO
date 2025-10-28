import json

class VendaItem:
    def __init__(self, id: int, q: int, p: float, Venda, Produto):
        self._id = id
        self.qtd = q
        self.preco = p
        self.IdVenda = Venda
        self.idProduto = Produto

    def __str__(self):
        if self.idProduto:
            produto_resposta = self.idProduto
        else:
            produto_resposta = "Sem Produto"
        if self.IdVenda:
            venda_resposta = self.IdVenda
        else:
            venda_resposta = "Sem Venda"
        return f"Id: {self._id} \nQuantidade: {self.qtd} \nPreço: {self.preco} \nVenda: {venda_resposta} \nProduto: {produto_resposta}"

class VendaItemDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj: VendaItem):

    @classmethod
    def listar(cls):

    @classmethod
    def listar_id(cls, id: VendaItem):

    @classmethod
    def atualizar(cls, obj: VendaItem):

    @classmethod
    def excluir(cls, obj: VendaItem):

    @classmethod
    def abrir(cls):

    @classmethod
    def salvar(cls):

