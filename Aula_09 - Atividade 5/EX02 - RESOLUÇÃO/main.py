from vendaitem import VendaItem, VendaItemDAO
from venda import Venda, VendaDAO
from cliente import Cliente, ClienteDAO
from produto import Produto, ProdutoDAO
from categoria import Categoria, CategoriaDAO

#--------------INSERÇÕES-------------------------------

cat1 = Categoria(0, 'Doces')
CategoriaDAO.inserir(cat1)


pro1 = Produto(0, 'Brigadeiro', 2.50, 100, cat1)
ProdutoDAO.inserir(pro1)


cli1 = Cliente(0, 'Raquel', 'raquel@gmail.com', '99999-9999')
ClienteDAO.inserir(cli1)

v1 = Venda(0, cli1)       # só passa ID e Cliente
v1.data = '2025-10-28'    # define a data depois
VendaDAO.inserir(v1)


vi1 = VendaItem(0, 10, pro1.preco, v1, pro1)  # preço unitário
VendaItemDAO.inserir(vi1)


#--------------MOSTRAR TUDO----------------------

print('Categorias:')
for c in CategoriaDAO.listar():
    print(c)

print('\nProdutos:')
for p in ProdutoDAO.listar():
    print(p)

print('\nClientes:')
for c in ClienteDAO.listar():
    print(c)

print('\nVendas:')
for v in VendaDAO.listar():
    print(v)

print('\nItens da Venda:')
for vi in VendaItemDAO.listar():
    print(vi)


# --- SALVAR TODOS OS DADOS EM JSON ---
CategoriaDAO.salvar()
ProdutoDAO.salvar()
ClienteDAO.salvar()
VendaDAO.salvar()
VendaItemDAO.salvar()

print("Dados salvos em JSON com sucesso!")
