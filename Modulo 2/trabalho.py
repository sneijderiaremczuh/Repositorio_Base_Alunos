import streamlit as st
st.sidebar.image('logo.png')
st.title('RH do tio ney - contrata mais que o vascão')



nome = st.text_input("digite seu nome")
idade = st.text_input("digite sua idade")
email = st.text_input("digite seu email")
salario = st.text_input("digite seu salario")
cargo = st.text_input("digite seu cargo")

if   st.button('cadastrar'):
     st.warning(f'o funcinario {nome}, foi contratado pelo tio ney👌')
     st.balloons()
     st.image('https://thispersondoesnotexist.com/')