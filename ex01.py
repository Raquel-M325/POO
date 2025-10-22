import datetime

class Cliente:
    def __init__(self, id: int, n: str, e: str, f: str):
        self._id = id
        self._nome = n
        self._email = e
        self._fone = f
    
    def set_id(self, id):
        if self._id < 0 or not isinstance(id, int):
            raise ValueError('Erro: ID Inválido')
        else:
            self._id = id

    def set_nome(self, n):
        if not isinstance(n, str):
            raise ValueError('Erro: Nome Inválido')
        else:
            self._nome = n

    def set_email(self, e):
        if not isinstance(e, str):
            raise ValueError('Erro: Email Inválido')
        else:
            self._email = e
    
    def set_fone(self, f):
        if not isinstance(f, str):
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

class Venda:
    def __init__(self, id: int, Cliente):
        self._id = id
        self.data = None
        self.carrinho = True
        self.total = 0.0
        self._IdCliente = Cliente

    def set_data(self, nova_data):  
        if not isinstance(nova_data, datetime.datetime):
            raise ValueError('Data inválida: deve ser um objeto datetime')
        
        self.data = nova_data


    def set_total(self, t):
        if t <= 0:
            raise ValueError('Erro: Está vazio')
        else:
            return self.total == self.t

    def calc_total(self):
        if self.total <= 0:
            self.carrinho = False
        return self.carrinho

    def get_data(self):
        return self.data

    def get_carrinho(self):
        return self.carrinho

    def get_total(self):
        return self.total


    def __str__(self):
        if self._IdCliente:
            self.cliente_resposta = self._IdCliente
        else:
            self.cliente_resposta = "Não há cliente"
        return f"Id: {self._id} \n Data: {self.data} \n Carrinho: {self.carrinho} \n Total: {self.total} \n Cliente: {self.cliente_resposta}"
    

        
class VendaItem:
    def __init__(self, id: int, q: int, p: float, Venda, Produto): #double é o "mesmo" do float
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
    def __init__(self, id: int, d: str, p: float, e: int, Categoria):
        self._id = id
        self.descricao = d
        self.preco = p
        self.estoque = e
        self.idCategoria = Categoria

    def set_preco(self, p):
        if p <= 0 or not isinstance(p, float):
            raise ValueError ('Preço Inválido')
        self.preco = p

    def set_estoque(self, e):
        if e <= 0 or not isinstance(e, int):
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
        if not isinstance(d, str):
            raise ValueError ('Erro: Tem que descrever o produto!')
        else:
            self.descricao = d

    def get_descricao(self):
        return self.descricao
    
    def __str__(self):
        return f"Id: {self._id} \n Descrição: {self.descricao}"
    
class UI: #IMCOMPLETO
    def __init__(self):
        self.categoria = []
        self.cliente = []
        self.venda = []
        self.produto = []
        self.vendaitem = []

    def setup_basico(self):

        id_cat = int(input())
        cat = Categoria(id, d)
        self.categoria.append(cat)

        pro = Produto(id, d, p, e, cat)
        self.produto.append(pro)

        cli = Cliente(id, n, e, f) #é solitário, não precisa de alguém para interligar, mas PRECISA CORRIGIR
        self.cliente.append(cli)

        ven = Venda(id, cli)
        self.venda.append(ven)

        venit = VendaItem(id, q, p, ven, pro)
        self.vendaitem.append(venit)

        return cat, pro, cli, ven, venit
    
ui = UI()
categoria, produto, cliente, venda, vendaitem = ui.setup_basico()

print(categoria)
print(produto)
print(cliente)
print(venda)
print(vendaitem)
        

    
        
        
