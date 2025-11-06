from cliente import Cliente, ClienteDAO
from produto import Produto, ProdutoDAO
from categoria import Categoria, CategoriaDAO #precisarei nomear a pasta para retomar como model


class View:
    def cliente_listar():
        return ClienteDAO.listar()

    def cliente_inserir(nome: str, email: str, fone:str):
        id = 0 #sempre vai ser fixo para inserir, tendo sempre o id
        c = Cliente(nome, email, fone)
        ClienteDAO.inserir(c) #nao tem return, porque esta inserindo, do qual nao precisa mostrar 

    def cliente_atualizar(id: int, nome: str, email:str, fone:str):
        c = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(c)

    def cliente_excluir(id:int):
        c = Cliente(id, '','','','') #somente o id para excluir
        ClienteDAO.excluir(c)
    
    def categoria_listar():
        return CategoriaDAO.listar()

    def categoria_inserir(descricao: str):
        id = 0
        c = Categoria(id, descricao)  #nao tem problema colocar id depois, mas sempre deve colocar
        CategoriaDAO.inserir(c)

    def categoria_atualizar(id: int, descricao: str):
        c = Categoria(id, descricao)
        CategoriaDAO.atualizar(c)

    def categoria_excluir(id: int):
        c = Categoria(id, '')
        CategoriaDAO.excluir(c)

    def produto_listar():
        return ProdutoDAO.listar()

    def produto_inserir(descricao: str, preco: float, estoque: int, idCategoria: int):
        id = 0
        p = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.inserir(p)

    def produto_atualizar(id: int, descricao: str, preco: float, estoque: int, idCategoria: int):
        p = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.atualizar(p)
        
    def produto_excluir(id: int):
        p = Produto(id, '', '', '', '')
        Produto.excluir(p)
        
    def produto_reajustar(percentual: float):
        for objs in ProdutoDAO.listar():
            obj.reajustar()
            ProdutoDAO.atualizar(obj)
    

    
