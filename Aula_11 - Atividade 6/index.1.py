import streamlit as st
from ex01 import Equacao

st.header("Equação de 2° Grau")
a = st.text_input("Informe o valor a")
b = st.text_input("Informe o valor b")
c = st.text_input("Informe o valor c")
x = st.text_input("Informe o valor x")

if st.button("Calcular"):
    try:
        e = Equacao(int(a), int(b), int(c))
        st.write(f"Equação y = {e.calc_y(int(x))}")
        st.write(f"Delta = {e.calc_delta()}")

        try:
            st.write(f"Bhaskara = {e.calc_bhaskara()}")
        
        except ValueError as err:
            st.warning(str(err))

    except Exception as erro:
        st.error(f"Erro: {erro}")
