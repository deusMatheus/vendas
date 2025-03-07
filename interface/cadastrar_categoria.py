import streamlit as st
from db_manager import db_manager as db
from categoria import Categoria
from funcionarios import Funcionarios
from log_manager import Log_manager as log

st.session_state['shopping_cart'] = []

def registerCategory(categoryName):
    if(st.session_state['operation']):
        Categoria().add_category(categoryName.capitalize())
        log().create_log('Categoria', Funcionarios().get_func_id_by_name(st.session_state['funcName']), f'Criação da Categoria {categoryName}')
        st.session_state['operation'] = False
        st.toast('Categoria cadastrada com sucesso!')
        st.toast('Categoria cadastrada com sucesso!')
        st.toast('Categoria cadastrada com sucesso!')

with st.form('register_category'):
    st.session_state['operation'] = True
    categoryName = st.text_input('Nome da categoria que deseja...')
    db().deleteValues('categorias', 'categoria', '""')
#    st.form_submit_button(label='CADASTRAR', on_click=registerCategory(categoryName))
    button = st.form_submit_button(label='Cadastrar')
    if (button):
        st.session_state['operation'] = True
        registerCategory(categoryName)

#    db().deleteValues('categorias', 'categoria', '""')
#    st.form_submit_button(label='EXCLUIR', on_click=deleteCategory(categoryName))
