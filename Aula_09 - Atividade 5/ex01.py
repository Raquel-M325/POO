import datetime

class Cliente:
    def __init__(self, id: int, n: str, e: str, f: str):
        self._id = id
        self._nome = n
        self._email = e
        self._fone = f
    
    def set_id(self, id):
        if self._id < 0 or self._id == str:
            raise ValueError('Erro: ID Inválido')
        else:
            self._id = id

    def set_nome(self, n):
        if self._nome == int:
            raise ValueError('Erro: Nome Inválido')
        else:
            self._nome = n

    def set_email(self, e):
        if self._email == int:
            raise ValueError('Erro: Email Inválido')
        else:
            self._email = e
    
    def set_fone(self, f):
        if self._fone == int:
            raise ValueError('Erro: Fone Inválido')
        else:
            self._fone = f

    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_email(self):
        return self._email
    
    def get_fone(self):
        return self._fone

    def __str__(self):
        return f"Id: {self._id} \n Nome: {self._nome} \n Email: {self._email} \n Fone: {self._fone}"

class Venda: #INCOMPLETO
    def __init__(self, id: int):
        self._id = id
        self.data = datetime
        self.carrinho = bool
        self.total = float
        self._IdCliente = Cliente

    # def set_data(self, datetime): tenho que analisar se isso faz sentido
    #     if self.data < 0 or self.data == 0:
    #         raise ValueError('Data Inválido')
    #     else:
    #         self.data = datetime

    def set_

    def __str__(self):
        return f""
    

        
class VendaItem: #INCOMPLETO
    def __init__(self, id: int, q: int, p: float): #double é o "mesmo" do float
        self._id = id
        self.qtd = q
        self.preco = p
        self.idVenda = Venda
        self.idProduto = Produto

    def set_qtd(self, q):
        if q <= 0:
            raise ValueError('Erro: Não há item quantidade')
        else:
            self.qtd = q

    def get_qtd(self):
        return self.qtd

    def __str__(self):
        if self.idProduto:
            self.produto_resposta = self.idProduto
        else: 
            self.produto_resposta = "Sem Produto"

        if self.idVenda:
            self.venda_resposta = self.idVenda
        else:
            self.venda_resposta = "Sem Venda"
        return f"Id: {self._id} \n Quantidade: {self.qtd} \n Preço: {self.preco} \n Venda: {self.venda_resposta} \n Produto: {self.produto_resposta}"
    
class Produto: 
    def __init__(self, id: int, d: str, p: float, e: int):
        self._id = id
        self.descricao = d
        self.preco = p
        self.estoque = e
        self.idCategoria = Categoria

    def set_preco(self, p):
        if p <= 0:
            raise ValueError ('Preço Inválido')
        else:
            self.preco = p

    def set_estoque(self, e):
        if e <= 0:
            raise ValueError('Erro: Acabou o estoque!')
        else:
            self.estoque = e
    
    def get_preco(self):
        return self.preco

    def get_estoque(self):
        return self.estoque

    def __str__(self):
        if self.idCategoria:
            self.categoria_resposta = self.idCategoria
        else:
           self.categoria_resposta = 'Sem Categoria' 
        return f"Id: {self._id} \n Descrição: {self.descricao} \n Preço: {self.preco} \n Estoque: {self.estoque} \n Categoria: {self.categoria_resposta}"

    
class Categoria: 
    def __init__(self, id: int, d: str):
        self._id = id
        self.descricao = d

    def set_descricao(self, d):
        if d == int:
            raise ValueError ('Erro: Tem que descrever o produto!')
        else:
            self.descricao = d

    def get_descricao(self):
        return self.descricao
    
    def __str__(self):
        return f"Id: {self._id} \n Descrição: {self.descricao}"
    

    

        

    
        
        
