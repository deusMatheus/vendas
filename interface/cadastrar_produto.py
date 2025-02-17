import streamlit as st
#from inferface import Interface
from categoria import Categoria
from produtos import Produtos

st.session_state['shopping_cart'] = []

def registerProduct(productName, productPrice, productCategory):
    if(productName != '' and st.session_state['operation']):
        try:
            Produtos().add_product(productName.capitalize(), productPrice, productCategory)
            st.write('Cadastro concluído!')
            st.toast('Produto cadastrado com sucesso!')
            st.toast('Produto cadastrado com sucesso!')
            st.toast('Produto cadastrado com sucesso!')
        except:
            st.write('')
        st.session_state['operation'] = False

#tabs = st.tabs(['Cadastrar', 'Excluir'])

#with tabs[0]: # Cadastrar
with st.form('register_product'):
    categorias = Categoria().get_categories_list()
    productName = st.text_input('Nome do produto')
    productPrice = st.number_input('Preço do produto (R$)', value=0.00, step=1.00)
#    productPrice = st.text_input('Preço do produto', value='R$ 0,00')
    productCategory = st.selectbox(
        'Escolha a categoria',
        categorias,
        placeholder='Escolha uma opção',
    )
#    st.form_submit_button(label='Cadastrar', on_click=registerProduct(productName, productPrice, productCategory))
    button = st.form_submit_button(label='Cadastrar')
    if (button):
        st.session_state['operation'] = True
        registerProduct(productName, productPrice, productCategory)


#with tabs[1]: # Excluir
#with st.form('delete_product'):
#    produtos = Produtos().get_product_list() #0 - id. 1 - nome. 2 - preço. 3 - categ_id
#        productName = st.text_input('Nome do produto')
#        productPrice = st.number_input('Preço do produto (R$)', value=0.00, step=1.00)
#    productPrice = st.text_input('Preço do produto', value='R$ 0,00')
#    products = st.selectbox(
#        'Escolha o produto',
#        produtos[1],
#        placeholder='Escolha uma opção',
#    )
#    st.form_submit_button(label='Excluir', on_click=deleteProduct(products))