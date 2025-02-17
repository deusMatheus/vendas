import streamlit as st
#from vendas import Vendas
from categoria import Categoria
from produtos import Produtos
from db_manager import db_manager as db

j = 0
categorias = db().selectTables(('categoria'), 'categorias')
#    categorias = Categoria().get_categories_list()
#    produtos = Produtos().get_product_list()

categories_string_list = []
shopping_cart = []

for category in categorias:
    if not category == None:
        categories_string_list.append(category[0])

if (not categories_string_list):
    st.write('Não há categorias ou produtos cadastrados! Primeiramente, cadastre uma categoria, e depois um produto.')

else:
#    with st.form('register_sale'):

    products_column, shopping_column = st.columns(2)

    with products_column:
        tabs = st.tabs(categories_string_list)
        buttons = []

        for i in range (len(tabs)):
            with tabs[i]:
                product_list = Produtos().list_item_by_category(categories_string_list[i])
                product_name = []
                product_price = []
                key_name = []

                for product in product_list:
                    product_price.append(product[1])
                    product_name.append(f'{product[0]}')

                for k in range(len(product_name)):
                    key_name = f'{product_name[k]}-{k}'
                    product_name[k] += f' - R${product_price[k]:.2f}'
                    st.write(product_name[k])
#                    st.write('Escolha a quantidade:')
                    st.number_input('Escolha a quantidade',0,99,step=1, key=j)
                    j += 1
                    st.divider()
                buttons.append(st.button(f'Adicionar {categories_string_list[i]}(s)'))
    
    with shopping_column:
        st.subheader('Itens no Carrinho de Venda')
        if(not shopping_cart):
            st.write('Não há produtos no carrinho.')
        else:
            st.button('Concluir venda')

    #            column_name = st.columns(1)

    #           with column_name:
    #            column_image, column_name = st.columns(2)
    #            column_name, column_price = st.columns(2)
    #            column_quantity,column_name, column_price = st.columns(3)
    #            columns_dict = {"col_quan": column_quantity, "col_name": column_name, "col_price": column_price}
    #            with column_quantity:
    #                for i in range (len(product_name)):

    #            with column_name:
    #                for i in range (len(product_name)):
    #                    st.write(product_name[i])
    #                    st.number_input('',0,99,step=1, key=key_name[i])
    #                    st.divider()

    #                for product in product_name:
    #                    st.write(product)

    #            with column_price:
    #                for price in product_price:
    #                    st.write(f'R${price:.2f}')

        