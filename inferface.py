import streamlit as st
from login_manager import Login_manager
from db_manager import db_manager as db
from funcionarios import Funcionarios
from produtos import Produtos
from categoria import Categoria
# A classe interface, posteriormente, será transformada para utilizar o streamlit

class Interface:

    def disable():
        st.session_state['disabled'] = True

    def mainPage(version):
        st.header(f'Sistema de Vendas {version}')
        if('funcName' in st.session_state and not st.session_state['funcName']):
            st.write(f'Usuário: {st.session_state['funcName']}')

    def loginScreen(version):
        privilege = 'nenhum'
        funcName = ''
        placeholder = st.empty()
        with placeholder.form('login_form', clear_on_submit=True):
            login_username = st.text_input('Username')
            login_password = st.text_input('Senha', type='password')
            submit_button = st.form_submit_button('Acessar')
            if(not Login_manager().check(login_username, login_password) and submit_button):
                st.write('Usuário ou senha incorretos.')
                submit_button = False
            elif(Login_manager().check(login_username, login_password) and submit_button):
                st.session_state['login'] = True
                privilege = Funcionarios().check_privileges(Funcionarios().get_func_id(login_username))
                funcName = Funcionarios().getName(login_username)
                placeholder.empty()
        return submit_button, privilege, funcName

#    def menuBar(version, funcName, privilege): # Antes de continuar, deve pegar uma flag dizendo se é adm ou funcionário. Deve fazer isso no retorn da loginScreen() 
#        if(privilege == 'adm'):
#            options = Interface.menuOption()
#            tabs = st.tabs(options)
#            with tabs[0]: # Realizar venda
#                Interface.tabs(funcName)
#
#            with tabs[1]: # Cadastrar produto
#                with st.form('register_product__'):
#                    categorias = Categoria().get_categories_list()
#                    productName = st.text_input('Nome do produto')
#                    productPrice = st.text_input('Preço do produto')
#                    productCategory = st.multiselect(
#                        'Escolha a categoria',
#                        categorias
#                    )
#                    st.form_submit_button('Cadastrar', on_click=Interface.registerProduct(productName, productPrice, productCategory))
##                    if(register_button):
##                        try:
##                            Produtos().add_product(productName, productPrice, productCategory)
##                            st.write('Cadastro concluído!')
##                        except:
##                            st.write('Um erro ocorreu.')
#
#
#            with tabs[2]: # Cadastrar categoria
#                pass
#
#            with tabs[3]: # Cadastrar funcionario
#                pass
#
#        else:
#            Interface.tabs(funcName)
#
#    def registerProduct(productName, productPrice, productCategory):
#        try:
#            Produtos().add_product(productName, productPrice, productCategory)
#            st.write('Cadastro concluído!')
#        except:
#            st.write('Um erro ocorreu.')

#        with st.sidebar:
#            pages = st.navigation([
#                st.Page('cadastrar_produtos.py', title='Cadastro de Produtos')
#            ])
#        pages.run()
#        with st.sidebar:
#            for option in options:
#                st.write(option)

#    def tabs(funcName):
#        st.write(f'Usuário: {funcName}')
#        st.divider()
#        categories = db().selectTables(('categoria'), 'categorias')
#        categories_string_list = []
#        for category in categories:
#            categories_string_list.append(category[0])
#
#        tabs = st.tabs(categories_string_list)
#        for i in range (len(tabs)):
#            with tabs[i]:
#                product_list = Produtos().list_item_by_category(categories_string_list[i])
#                product_name = []
#                product_price = []
#
#                for product in product_list:
#                    product_name.append(product[0])
#                    product_price.append(product[1])
#                colum_name, column_price = st.columns(2)
#
#                with colum_name:
#                    for product in product_name:
#                        st.write(product)
#
#                with column_price:
#                    for price in product_price:
#                        st.write(f'R${price:.2f}')

    def wrongUserPassword():
        st.write('Usuário ou senha incorretos!')

    def loginScreen2(version):
        message = f'Sistema de Vendas V{version}'
        return f'{"*"*len(message)}\n{message}\n{"*"*len(message)}'
    
    def askForLogin():
        return input('Digite seu username: ')
    
    def askforPassword():
        return input('Digite sua senha: ')
    
    def userLogin(flag, name):
        if(flag):
            return f'Login realizado como {name}!'
        else:
            return f'Usuário ou senha incorretos!'

    def menu2(name):
        welcome_message = f'Bem vindo(a) {name}!'
        full_message = f'''
        Qual das opções abaixo deseja?
        1 - Realizar venda
        2 - Listar produtos
        3 - Listar categorias
        4 - Listar vendas por funcionário
        5 - Cadastrar produto
        6 - Cadastrar categoria
        7 - Cadastrar funcionário
        0 - Logout
        * - Encerrar programa'''
        return f'{"*"*len(welcome_message)*2}\n{welcome_message}{full_message}\n{"*"*len(welcome_message)*2}'

    def menuOption():
        return ['Realizar venda', 'Cadastrar produto', 'Cadastrar categoria', 'Cadastrar funcionário']

    def inputMenu():
        return input('>>> ')