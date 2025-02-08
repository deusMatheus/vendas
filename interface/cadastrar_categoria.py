import streamlit as st
from db_manager import db_manager as db
from categoria import Categoria

def registerCategory(categoryName):
    Categoria().add_category(categoryName)

def deleteCategory(categoryName):
    Categoria().delete_category(categoryName)

with st.form('register_category'):
    categoryName = st.text_input('Nome da categoria que deseja...')
    db().deleteValues('categorias', 'categoria', '""')
    st.form_submit_button(label='CADASTRAR', on_click=registerCategory(categoryName))
    db().deleteValues('categorias', 'categoria', '""')
    st.form_submit_button(label='EXCLUIR', on_click=deleteCategory(categoryName))
