import streamlit as st
from db_manager import db_manager as db
from produtos import Produtos

st.session_state['shopping_cart'] = []

#st.write(f'Usuário: {st.session_state['funcName']}')
categories = db().selectTables(('categoria'), 'categorias')
categories_string_list = []
for category in categories:
    categories_string_list.append(category[0])

if (not categories_string_list):
    st.write('Não há categorias ou produtos cadastrados! Primeiramente, cadastre uma categoria, e depois um produto.')

else:
    tabs = st.tabs(categories_string_list)
    for i in range (len(tabs)):
        with tabs[i]:
            product_list = Produtos().list_item_by_category(categories_string_list[i])
            product_name = []
            product_price = []

            for product in product_list:
                product_name.append(product[0])
                product_price.append(product[1])
            column_name, column_price = st.columns(2)

            with column_name:
                for product in product_name:
                    st.write(product)

            with column_price:
                for price in product_price:
                    st.write(f'R${price:.2f}')
