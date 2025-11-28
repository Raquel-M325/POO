import streamlit as st
import Aula09_Atividade_5.views from View
import pandas as pd 

class ManterClienteUI: #não está completo, mas tem o professor para ver!
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    def listar():
        clientes = View.cliente_listar()   
        #for cliente in clientes: st.write(cliente)
        if len(clientes) == 0: st.write("Nenhum cliente encontrado")
        else:
            list_dic = []
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "nome", "email", "fone", "senha"])


    def inserir():  
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o email")
        fone = st.text_input("Informe o telefone")
        senha = st.text_input("Informe a senha")
        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone, senha)
            st.sucess()
        st.write("Inserir")
        
    def atualizar():
        st.write("Atualizar")

        
    def excluir():
        st.write("Inserir")

