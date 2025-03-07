import streamlit as st
import datetime
from log_manager import Log_manager as log
from vendas import Vendas
from funcionarios import Funcionarios
from categoria import Categoria
from produtos import Produtos
from db_manager import db_manager as db
from time import sleep

buttons_to_remove = []

if not st.session_state['shopping_cart']:
    shopping_cart = []

#def write_on_screen(itemQuantity, itemName, itemPrice):
#    st.write(f'{itemQuantity}x {itemName} - R${(float(itemQuantity) * float(itemPrice)):.2f}')
#    st.write(f'Preço unitário: R${itemPrice}')

#def write_on_screen():
#    final_price = 0
#    for item in st.session_state['shopping_cart']:
#        st.write(f'{item[1]}x {item[0]} - R${(float(item[1]) * float(item[2])):.2f}')
#        st.write(f'Preço unitário: R${item[2]}')
#        buttons_to_remove.append([st.button(f'Remover {item[1]}x {item[0]}'), [item[0], item[1], item[2]]])
#        st.divider()
#        final_price += float(item[2]) * float(item[1])
#    return final_price

def add_to_shopping_cart(productName, productQuantity, productPrice):
    for item in st.session_state['shopping_cart']:
        if(productName in item):
            item[1] += productQuantity
            return True
    st.session_state['shopping_cart'].append([productName, productQuantity, productPrice])
#    print(st.session_state['shopping_cart'])

def remove_from_shopping_cart(productName, productQuantity, productPrice):
    st.session_state['shopping_cart'].remove([productName, productQuantity, productPrice])
    st.switch_page('interface/realizar_venda.py')

categorias = Categoria().get_categories_list()
categories_string_list = []

for category in categorias:
    if not category == None:
        categories_string_list.append(category)

if (not categories_string_list):
    st.write('Não há categorias ou produtos cadastrados! Primeiramente, cadastre uma categoria, e depois um produto.')

else:
    products_column, shopping_column = st.columns(2)

    with products_column:
        tabs = st.tabs(categories_string_list)
        buttons = []
        product_keys = {}

        for i in range (len(tabs)):
            temp_products = []
            with tabs[i]:
                product_list = Produtos().list_item_by_category(categories_string_list[i])
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
                    st.number_input('Escolha a quantidade',0,99,step=1, key=f'{product_name[k]}')
                    st.divider()
                product_keys[categories_string_list[i]] = temp_products
                buttons.append(st.button(f'Adicionar {categories_string_list[i]}'))

        if(True in buttons):
            for i in range (len(buttons)):
                if(buttons[i]):
                    for product_key in product_keys[categories_string_list[i]]:
                        product_name_to_cart, product_price_to_cart = product_key.split('-')
                        product_quantity_to_cart = st.session_state[product_key]
                        if(product_quantity_to_cart>0):
                            add_to_shopping_cart(product_name_to_cart, product_quantity_to_cart, product_price_to_cart[3:])

    with shopping_column:
        st.subheader(':shopping_trolley: Carrinho')
        buttons_to_remove = []
        if(not st.session_state['shopping_cart']):
            st.write('Não há produtos no carrinho.')

        else:
            final_price = 0
#            write_on_screen()

            for item in st.session_state['shopping_cart']:
                st.write(f'{item[1]}x {item[0]} - R${(float(item[1]) * float(item[2])):.2f}')
                st.write(f'Preço unitário: R${item[2]}')
                buttons_to_remove.append([st.button(f'Remover {item[1]}x {item[0]}'), [item[0], item[1], item[2]]])
                st.divider()
                final_price += float(item[2]) * float(item[1])

            st.write(f'Preço total: R${final_price:.2f}')
            finish_sale = st.button('Concluir venda')
            if(finish_sale):
                funcID = Funcionarios().get_func_id_by_name(st.session_state['funcName'])
                shopping_cart = st.session_state['shopping_cart']
                sale_datetime = datetime.datetime.now()
                formatted_sale_datetime = sale_datetime.strftime('%d/%m/%Y-%H:%M:%S')
                shoppingCartIDs = ', '.join([f"{Produtos().get_product_id(item[0][:-1])}" for item in shopping_cart])
                for item in shopping_cart:
                    productID_ = Produtos().get_product_id(item[0][:-1])
                    Vendas().add_sale(productID_,item[1],float(item[2])*int(item[1]),funcID,shoppingCartIDs,formatted_sale_datetime)
                st.success('Venda concluída com sucesso!!')
                log().create_log('Vendas', funcID, f'Venda realizada no valor de R${final_price:.2f} por {Funcionarios().getNameById(funcID)}')
                for i in range(3,0,-1):
                    st.toast(f'Retornando ao menu principal em {i}')
                    sleep(1)
                st.session_state['shopping_cart'] = []
                st.switch_page('interface/menu_principal.py')

        for i in range (len(buttons_to_remove)):
            if(True in buttons_to_remove[i]):
                if(buttons_to_remove[i][0]):
#                    print(st.session_state)
                    remove_from_shopping_cart(buttons_to_remove[i][1][0], buttons_to_remove[i][1][1], buttons_to_remove[i][1][2]) # É feito desta forma pois buttons_to_remove possui a seguinte estrutura: [[False, ['ITEM1_NAME', ITEM1_QUANTITY, 'ITEM1_VALUE']], [False, ['ITEM2_NAME', ITEM2_QUANTITY, 'ITEM2_VALUE']], ...]
#                    write_on_screen()
