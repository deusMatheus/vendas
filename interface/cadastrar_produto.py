import streamlit as st
#from inferface import Interface
from categoria import Categoria
from produtos import Produtos

def registerProduct(productName, productPrice, productCategory):
    try:
        Produtos().add_product(productName, productPrice, productCategory)
        st.write('Cadastro concluído!')
    except:
        st.write('Um erro ocorreu.')

with st.form('register_product'):
    categorias = Categoria().get_categories_list()
    productName = st.text_input('Nome do produto')
    productPrice = st.text_input('Preço do produto')
    productCategory = st.selectbox(
        'Escolha a categoria',
        categorias
    )
    st.write(productCategory)
    st.form_submit_button(label='Cadastrar', on_click=registerProduct(productName, productPrice, productCategory))

