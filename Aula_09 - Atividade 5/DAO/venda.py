import json

class Venda:
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

class VendaDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj: Venda):

    @classmethod
    def listar(cls):

    @classmethod
    def listar_id(cls, id: Venda):

    @classmethod
    def atualizar(cls, obj: Venda):

    @classmethod
    def excluir(cls, obj: Venda):

    @classmethod
    def abrir(cls):

    @classmethod
    def salvar(cls):