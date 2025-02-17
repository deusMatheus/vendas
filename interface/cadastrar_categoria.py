import streamlit as st
from db_manager import db_manager as db
from categoria import Categoria

st.session_state['shopping_cart'] = []

def registerCategory(categoryName):
    if(st.session_state['operation']):
        Categoria().add_category(categoryName.capitalize())
        st.session_state['operation'] = False
        st.toast('Categoria cadastrada com sucesso!')
        st.toast('Categoria cadastrada com sucesso!')
        st.toast('Categoria cadastrada com sucesso!')

with st.form('register_category'):
    st.session_state['operation'] = True
    categoryName = st.text_input('Nome da categoria que deseja...')
    db().deleteValues('categorias', 'categoria', '""')
#    st.form_submit_button(label='CADASTRAR', on_click=registerCategory(categoryName))
    button = st.form_submit_button(label='CADASTRAR')
    if (button):
        st.session_state['operation'] = True
        registerCategory(categoryName)

#    db().deleteValues('categorias', 'categoria', '""')
#    st.form_submit_button(label='EXCLUIR', on_click=deleteCategory(categoryName))
