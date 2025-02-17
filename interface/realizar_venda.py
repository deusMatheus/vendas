import streamlit as st
#from vendas import Vendas
from categoria import Categoria
from produtos import Produtos
from db_manager import db_manager as db

if not st.session_state['shopping_cart']:
    shopping_cart = []

def add_to_shopping_cart(productName, productQuantity, productPrice):
    st.session_state['shopping_cart'].append([productName, productQuantity, productPrice])
#    st.session_state['shopping_cart'] = True
#    st.write(f'Nome do produto: {productName}')
#    st.write(f'Preço do produto: {productPrice}')
#    st.write(f'Quantidade do produto: {productQuantity}')
#    shopping_cart.append([productName, productQuantity, productPrice])

#j = 0
categorias = Categoria().get_categories_list()
#categorias = db().selectTables(('categoria'), 'categorias')
#    categorias = Categoria().get_categories_list()
#    produtos = Produtos().get_product_list()

categories_string_list = []

for category in categorias:
    if not category == None:
        categories_string_list.append(category)

if (not categories_string_list):
    st.write('Não há categorias ou produtos cadastrados! Primeiramente, cadastre uma categoria, e depois um produto.')

else:
#    with st.form('register_sale'):

    products_column, shopping_column = st.columns(2)

    with products_column:
        tabs = st.tabs(categories_string_list)
        buttons = []
        product_keys = {}


        for i in range (len(tabs)):
            temp_products = []
            with tabs[i]:
                product_list = Produtos().list_item_by_category(categories_string_list[i])
#                print(product_list)
                product_name = []
                product_price = []

                for product in product_list:
                    product_name.append(f'{product[0]}')
                    product_price.append(product[1])

                for k in range(len(product_name)):
                    key_name = f'{product_name[k]}-{k}'
                    product_name[k] += f' - R${product_price[k]:.2f}'
                    st.write(product_name[k])
                    temp_products.append(product_name[k])
#                    product_keys[product_name[k]] = categories_string_list[i]
#                    st.write('Escolha a quantidade:')
#                    st.number_input('Escolha a quantidade',0,99,step=1, key=j)
                    st.number_input('Escolha a quantidade',0,99,step=1, key=f'{product_name[k]}')
#                    j += 1
                    st.divider()
                product_keys[categories_string_list[i]] = temp_products
                buttons.append(st.button(f'Adicionar {categories_string_list[i]}'))
#        print(st.session_state)
#        print(f'Teste: {product_keys}')
        if(True in buttons):
            for i in range (len(buttons)):
                if(buttons[i]):
#                    print(f'product_keys[categories_string_list[i]]: {product_keys[categories_string_list[i]]}')
                    for product_key in product_keys[categories_string_list[i]]:
                        product_name_to_cart, product_price_to_cart = product_key.split('-')
                        product_quantity_to_cart = st.session_state[product_key]
                        if(product_quantity_to_cart>0):
                            add_to_shopping_cart(product_name_to_cart, product_quantity_to_cart, product_price_to_cart[3:])
#                        print(f'product_key: {product_key}')
#                        print(f'Nome do Produto: {product_name_to_cart}')
#                        print(f'Preço do Produto: {float(product_price_to_cart[3:])}')
#                        print(f'Quantidade: {product_quantity_to_cart}')
#                    print(f'product_key.split("-"): {product_key.split('-')}')
#                    print(f'categories_string_list[i]: {categories_string_list[i]}')
#                    print(f'st.session_state: {st.session_state}')
#                    print(f'product_keys: {product_keys}')
    
    with shopping_column:
#        print(st.session_state['shopping_cart'])
        st.subheader(':shopping_trolley: Carrinho')
        if(not st.session_state['shopping_cart']):
            st.write('Não há produtos no carrinho.')
        else:
            final_price = 0
            for item in st.session_state['shopping_cart']:
                st.write(f'{item[1]} x {item[0]} - R${(float(item[1]) * float(item[2])):.2f}')
#                st.write(f'Produto: {item[0]}')
#                st.write(f'Quantidade: {item[1]}')
                st.write(f'Preço unitário: R${item[2]}')
                st.divider()
#                st.write(f'Valor por itens: {float(item[1]) * float(item[2])}')
                final_price += float(item[2]) * float(item[1])
            st.write(f'Preço total: R${final_price:.2f}')
            finish_sale = st.button('Concluir venda')
            if(finish_sale):

#                '''
#               PENSAR NA PROTEÇÃO
#               Encapsulamento em Classes? Daria pra aplicar nas funções e variáveis do streamlit se usadas em conjunto?
#
#               productID = ??? FAZER Produtos().getFuncId(productNname) 
#               quantity = ??? FAZER
#               totalValue = ?final_price?
#               funcID = ??? FAZER Funcionarios().getFuncId(name) ???
#               sale_datetime = datetime.datetime.now()
#               formatted_sale_datetime = sale_datetime.strftime('%d/%m/%Y-%H:%M:%S')
#               for item in shoppingCart:
#                   self.add_sale(productID,quantity,totalValue, funcID, shoppingCartIDs, formatted_sale_datetime)
#                               
#           '''

                st.success('Venda concluída com sucesso!!')
                st.session_state['shopping_cart'] = []

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

        