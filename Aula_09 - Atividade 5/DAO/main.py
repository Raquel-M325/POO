from vendaitem import VendaItem, VendaItemDAO
from venda import Venda, VendaDAO
from cliente import Cliente, ClienteDAO
from produto import Produto, ProdutoDAO
from categoria import Categoria, CategoriaDAO


#--------------CHAMADO-------------------------------
vi1 = VendaItem(0, 10, pro1.preco * 10, v1, pro1)
VendaItemDAO.inserir(vi1)

v1 = Venda(0, cli1, '2025-10-28')
VendaDAO.inserir(v1)

cli1 = Cliente(0, 'Raquel', 'raquel@gmail.com', '99999-9999)
Cliente.inserir(cli1)

pro1 = Produto(0, 'Brigadeiro', 2.50, 100, cat1)
ProdutoDAO(pro1)

cat1 = Categoria(0, 'Doces')
CategoriaDAO.inserir(cat1)

#--------------MOSTRAR TUDO----------------------
print('Categorias:')
for c in CategoriasDAO.listar():
  print(c)

print(\n'Produto:')
for p in ProdutoDAO.listar():
  print(p)

print(\n'Clientes:')
for c in ClientesDAO.listar():
  print(c)

print(\n'Venda:')
for v in VendaDAO.listar():
  print(v)

print(\n'Itens da Venda:')
for vi in VendaItemDAO:
  print(vi)

