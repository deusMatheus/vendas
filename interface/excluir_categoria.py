import streamlit as st
#from db_manager import db_manager as db
from categoria import Categoria
from funcionarios import Funcionarios
from log_manager import Log_manager as log

st.session_state['shopping_cart'] = []

def deleteCategory(categoryName):
    if(st.session_state['operation']):
        Categoria().delete_category(categoryName)
        log().create_log('Categoria', Funcionarios().get_func_id_by_name(st.session_state['funcName']), f'Exclusão da Categoria {categoryName}')
        st.session_state['operation'] = False
        st.toast('Categoria excluída com sucesso!')
        st.toast('Categoria excluída com sucesso!')
        st.toast('Categoria excluída com sucesso!')

with st.form('delete_category'): # Set default value to not automatically delete
    categoriesList = Categoria().get_categories_list()
    categoriesList_ = ['Escolha uma opção']
    for category in categoriesList:
        categoriesList_.append(category)

    categories = st.selectbox (
        'Escolha a categoria que deseja excluir',
        categoriesList_,
        placeholder='Escolha uma opção',      
    )
#    st.form_submit_button(label='EXCLUIR', on_click=deleteCategory(categories))
    button = st.form_submit_button(label='Excluir')
    if(button):
        st.session_state['operation'] = True
        deleteCategory(categories)
