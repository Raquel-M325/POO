from cliente import Cliente, ClienteDAO
from produto import Produto, ProdutoDAO
from categoria import Categoria, CategoriaDAO #precisarei nomear a pasta para retomar como model


class View:
    def cliente_listar():
        return ClienteDAO.listar()

    def cliente_inserir(nome: str, email: str, fone:str):
        id = 0
        return

    def cliente_atualizar(id: int, nome: str, email:str, fone:str):


    def cliente_excluir(id:int):


    def categoria_listar():
        return CategoriaDAO.listar()

    def categoria_inserir(descricao: str):


    def categoria_atualizar(id: int, descricao: str):


    def categoria_excluir(id: int):


    def produto_listar():
        return ProdutoDAO.listar()

    def produto_inserir(descricao: str, preco: float, estoque: int, idCategoria: int):


    def produto_atualizar(id: int, descricao: str, preco: float, estoque: int, idCategoria: int):


    def produto_excluir(id: int):


    def produto_reajustar(percentual: float):


    
