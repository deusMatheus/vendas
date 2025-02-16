import streamlit as st
#from inferface import Interface
from categoria import Categoria
from produtos import Produtos

def registerProduct(productName, productPrice, productCategory):
    try:
        Produtos().add_product(productName, productPrice, productCategory)
        st.write('Cadastro concluído!')
    except:
        st.write('')

with st.form('register_product'):

    tabs = st.tabs(['Registrar', 'Excluir'])

    with tabs[0]: # Registrar

        categorias = Categoria().get_categories_list()
        productName = st.text_input('Nome do produto')
        productPrice = st.number_input('Preço do produto (R$)', value=0.00, step=1.00)
    #    productPrice = st.text_input('Preço do produto', value='R$ 0,00')
        productCategory = st.selectbox(
            'Escolha a categoria',
            categorias,
            placeholder='Escolha uma opção',
        )
        st.form_submit_button(label='Cadastrar', on_click=registerProduct(productName, productPrice, productCategory))

    with tabs[1]: # Excluir
        pass