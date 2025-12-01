import streamlit as st
from Aula_12.mantercategoria import ManterCategoriaUI
from Aula_12.mantercliente import ManterClienteUI
from Aula_12.manterproduto import ManterProdutoUI
from Aula_12.reajustarproduto import ReajustarProdutoUI
from Aula_12.login import LoginUI


class IndexUI:
    def menu_admin(): 
        op = st.sidebar.selectbox("Menu",[
        "Cadastro de Categorias",
        "Cadastro de Clientes", 
        "Cadastro de Produtos",
        "Reajustar Produtos"])

        st.session_state["opcao"] = op
        if op == "Cadastro de Categorias": ManterCategoriaUI.main()
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Produtos" : ManterProdutoUI.main()
        if op == "Reajustar Produtos": ReajustarProdutoUI.main()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", [
            "Entrar no sistema",
            "Abrir conta"
        ])

        if op == "Entrar no sistema": LoginUI.main()
        if op == "Abrir conta": pass


    def menu_cliente():
        op = st.sidebar.selectbox("Menu", [
            "Listar produtos",
            "Inserir produto no carrinho",
            "Comprar carrinho",
            "Listar minhas compras"])
        
        if op == "Listar produtos": #incompleto
        if op == "Inserir produto no carrinho":
        if op == "Comprar carrinho":
        if op == "Listar minhas compras":

    def sidebar():
        if "cliente_id" not in st.session_state: IndexUI.menu_visitante()
        else: 
            st.sidebar.write("Bem-vindo" + st.session_state["cliente_nome"])
            admin = st.session_state["cliente_nome"] == "admin"
            if admin: IndexUI.menu_admin()
            IndexUI.menu_admin()
            IndexUI.sair_do_sistema

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()

    def main():
        # if "op" not in st.session_state: st.session_state["opcao"] = []
        # st.write(st.session_state)
        View.cliente_criar_admin() #verifica se existe o usuario admin
        IndexUI.sidebar() #mostra o menu lateral
        
IndexUI.main()