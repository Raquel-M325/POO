import datetime

# --- CLASSE CLIENTE ---
class Cliente:
    def __init__(self, id: int, n: str, e: str, f: str):
        self._id = id
        self._nome = n
        self._email = e
        self._fone = f

    def reajustar(self, percentual):
        self.preco = self.preco * (1 + percentual / 100)
    
    def set_id(self, id):
        if id < 0 or not isinstance(id, int):
            raise ValueError('Erro: ID Inválido')
        self._id = id

    def set_nome(self, n):
        if not isinstance(n, str):
            raise ValueError('Erro: Nome Inválido')
        self._nome = n

    def set_email(self, e):
        if not isinstance(e, str):
            raise ValueError('Erro: Email Inválido')
        self._email = e
    
    def set_fone(self, f):
        if not isinstance(f, str):
            raise ValueError('Erro: Fone Inválido')
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
        return f"Id: {self._id} \nNome: {self._nome} \nEmail: {self._email} \nFone: {self._fone}"


# --- CLASSE PRODUTO ---
class Produto:
    def __init__(self, id: int, d: str, p: float, e: int, Categoria):
        self._id = id
        self.descricao = d
        self.preco = p
        self.estoque = e
        self.idCategoria = Categoria

    def set_preco(self, p):
        if p <= 0 or not isinstance(p, float):
            raise ValueError('Preço Inválido')
        self.preco = p

    def set_estoque(self, e):
        if e < 0 or not isinstance(e, int):
            raise ValueError('Erro: Estoque inválido')
        self.estoque = e

    def atualizar_estoque(self, qtd):
        if qtd > self.estoque:
            raise ValueError("Quantidade maior que estoque disponível")
        self.estoque -= qtd
        return self.estoque

    def get_preco(self):
        return self.preco

    def get_estoque(self):
        return self.estoque

    def __str__(self):
        if self.idCategoria:
            categoria_resposta = self.idCategoria
        else:
            categoria_resposta = 'Sem Categoria'
        return f"Id: {self._id} \nDescrição: {self.descricao} \nPreço: {self.preco} \nEstoque: {self.estoque} \nCategoria: {categoria_resposta}"


# --- CLASSE CATEGORIA ---
class Categoria:
    def __init__(self, id: int, d: str):
        self._id = id
        self.descricao = d

    def set_descricao(self, d):
        if not isinstance(d, str):
            raise ValueError('Erro: Tem que descrever o produto!')
        self.descricao = d

    def get_descricao(self):
        return self.descricao

    def __str__(self):
        return f"Id: {self._id} \nDescrição: {self.descricao}"


# --- CLASSE VENDA ---
class Venda:
    def __init__(self, id: int, Cliente):
        self._id = id
        self.data = None
        self.carrinho = True
        self.total = 0.0
        self._IdCliente = Cliente
        self.itens = [] # Lista de VendaItem para somar total

    def set_id(self, id):
        if id < 0 or not isinstance(id, int):
            raise ValueError('Erro: ID Inválido')
        self._id = id

    def set_data(self, nova_data):
        if not isinstance(nova_data, datetime.datetime):
            raise ValueError('Data inválida: deve ser um objeto datetime')
        self.data = nova_data

    def calc_total(self):
        self.total = sum(item.calc_preco() for item in self.itens)
        return self.total

    def set_carrinho(self):
        if self.total <= 0:
            self.carrinho = False
            print('Não há carrinho')
        else:
            self.carrinho = True
            pergunta = input('Quer comprar? [y/n]: ')
            while pergunta == 'n':
                pergunta = input('Quer comprar? [y/n]: ')
        return self.total

    def get_data(self):
        return self.data

    def get_carrinho(self):
        return self.carrinho

    def get_total(self):
        return self.total

    def __str__(self):
        if self._IdCliente:
            cliente_resposta = self._IdCliente
        else:
            cliente_resposta = "Não há cliente"
        return f"Id: {self._id} \nData: {self.data} \nCarrinho: {self.carrinho} \nTotal: {self.total} \nCliente: {cliente_resposta}"


# --- CLASSE VENDA ITEM ---
class VendaItem:
    def __init__(self, id: int, q: int, p: float, Venda, Produto):
        self._id = id
        self.qtd = q
        self.preco = p
        self.IdVenda = Venda
        self.idProduto = Produto

    def set_id(self, id):
        if id < 0 or not isinstance(id, int):
            raise ValueError('Erro: ID Inválido')
        self._id = id

    def set_qtd(self, q):
        if q <= 0:
            raise ValueError('Erro: Não há item quantidade')
        self.qtd = q

    def set_preco(self, p):
        if p <= 0:
            raise ValueError('Erro: Não tem preço')
        self.preco = p

    def calc_preco(self):
        self.preco = self.qtd * self.idProduto.preco
        return self.preco

    def get_id(self):
        return self._id

    def get_preco(self):
        return self.preco

    def get_qtd(self):
        return self.qtd

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


# --- CLASSE UI ---
class UI:
    def __init__(self):
        self.categoria = []
        self.cliente = []
        self.venda = []
        self.produto = []
        self.vendaitem = []

    def setup_basico(self):
        # Criar Cliente
        cli = Cliente(1, 'Raquel', 'raquel@gmail.com', '98775-4555')
        self.cliente.append(cli)

        # Criar Produtos
        p1 = Produto(1, 'Café 3 corações', 10.0, 100, None)
        p2 = Produto(2, 'Coca-cola', 5.0, 20, None)
        self.produto.extend([p1, p2])

        # Criar Venda
        ven = Venda(1, cli)
        self.venda.append(ven)

        # Criar VendaItem
        vi1 = VendaItem(1, 5, p1.preco, ven, p1)
        vi2 = VendaItem(2, 3, p2.preco, ven, p2)
        self.vendaitem.extend([vi1, vi2])

        # Associar itens à venda
        ven.itens.extend([vi1, vi2])
        ven.calc_total() # Calcula total da venda

        # Atualizar estoque automaticamente
        for item in ven.itens:
            item.idProduto.atualizar_estoque(item.qtd)

        # Criar Categorias por último
        c1 = Categoria(1, 'Alimentos e bebidas')
        c2 = Categoria(2, 'Bebê')
        c3 = Categoria(3, 'Automotivo')
        self.categoria.extend([c1, c2, c3])

        return cli, p1, p2, ven, vi1, vi2, c1, c2, c3


# --- EXECUÇÃO ---
ui = UI()
cliente, produto1, produto2, venda, vi1, vi2, c1, c2, c3 = ui.setup_basico()

print("\n--- INICIANDO PROCESSO DE COMPRA ---")
venda.set_carrinho() 
print("--- PROCESSO DE COMPRA FINALIZADO ---\n")

# --- TESTE ---
print(cliente)
print(produto1)
print(produto2)
print(venda)
print(vi1)
print(vi2)
print(c1)
print(c2)
print(c3)
