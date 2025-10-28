import json

class Produto:
    def __init__(self, id: int, d: str, p: float, e: int, Categoria):
        self._id = id
        self.descricao = d
        self.preco = p
        self.estoque = e
        self.idCategoria = Categoria

     def __str__(self):
        if self.idCategoria:
            categoria_resposta = self.idCategoria
        else:
            categoria_resposta = 'Sem Categoria'
        return f"Id: {self._id} \nDescrição: {self.descricao} \nPreço: {self.preco} \nEstoque: {self.estoque} \nCategoria: {categoria_resposta}"

class ProdutoDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj: Produto):

    @classmethod
    def listar(cls):

    @classmethod
    def listar_id(cls, id: int):

    @classmethod
    def atualizar(cls, obj: Produto):

    @classmethod
    def excluir(cls, obj: Produto):

    @classmethod
    def abrir(cls):

    @classmethod
    def salvar(cls):

    