import streamlit as st
#from inferface import Interface
from categoria import Categoria
from produtos import Produtos

def deleteProduct(productName):
    if(st.session_state['operation']):
        Produtos().delete_product(productName)
        st.session_state['operation'] = False
        st.toast('Produto excluído com sucesso!')
        st.toast('Produto excluído com sucesso!')
        st.toast('Produto excluído com sucesso!')


with st.form('delete_product'): # Set default value to not automatically delete
    produtos = Produtos().get_product_list() #0 - id. 1 - nome. 2 - preço. 3 - categ_id
    produtos_ = ['Escolha uma opção']
    for produto in produtos[1]:
        produtos_.append(produto)

    products = st.selectbox(
        'Escolha o produto que deseja excluir',
        produtos_,
        placeholder='Escolha uma opção',
    )
#    st.form_submit_button(label='Excluir', on_click=deleteProduct(products))
    button = st.form_submit_button(label='Excluir')
    if(button):
        st.session_state['operation'] = True
        deleteProduct(products)