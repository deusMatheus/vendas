from inferface import Interface
from login_manager import Login_manager
from funcionarios import Funcionarios
from produtos import Produtos
from vendas import Vendas
from categoria import Categoria
from db_manager import db_manager as db
from time import sleep
import streamlit as st

version = '0.5'

# Com este CSS é possível estilizar a página pegando as classes dos componentes. 
#with open ('styles/styles.css') as file:
#    css = file.read()
#
#st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

#'''
#------ ######################################################
#---------------- Sistema de Vendas V0.5 ----------------
#------ Esta aplicação é um sistema de vendas, onde armazena as informações em banco de dados utilizando sqlite. 
#------ Futuramente serão implementadas duas interfaces, uma para funcionários e outra para clientes.
#------ Os clientes poderão visualizar os itens disponíveis como num cardápio digital, separados por categorias.
#------ Inicialmente, a interface será através do terminal, mas posteriormente deve ser atualizada para utilizar o streamlit
#------ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#------ Documentar melhor as funções do código, especialmente a função Vendas().sale(self, funcID)
#------ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#------ ######################################################
#---------------- Para V0.6 ----------------
#------ Passar para o db os dados resgatados da página em realizar_venda.py
#------ (WIP - 0.7) Pensar na segurança dos dados e como fazer o encapsulamento destas informações com classes, até mesmo nas interfaces do streamlit
#------ ######################################################
#---------------- Concluído V0.5 ----------------
#------ Implementar o sistema de vendas adicionando os produtos no carrinho
#------ ######################################################
#---------------- Concluído V0.4 ----------------
#------ Começar a trabalhar na interface com o Streamlit
#------ Ao invés de criar funções específicas através do arquivo Interface, criar páginas 
#------ específicas para cada página.
#------ ######################################################
#---------------- Concluído V0.3 ----------------
#------ Criar opção de logout e retornar para o menu de login.
#------ Funcionários realizam somente vendas.
#------ Funcionários com privilégios de ADM podem adicionar e excluir funcionários e produtos. Além disso, podem também listar as vendas e organizar por funcionários.
#------ ######################################################
#---------------- V0.2.1 ----------------
#------ Criar um sistema, utilizando DBs e funções para que através da interface seja possível adicionar e retirar itens. 
#------ Criar um sistema de login e senha para funcionários
#------ A tabela Funcionários deve possuir uma coluna de privilégios. Administradores recebem o privilégio adm, e funcionários não possuem privilégios. 
#------ A tabela Vendas deve possuir uma coluna id_funcionário que representa o funcionário que realizou a transação
#------ A tabela Produtos deve possuir uma coluna categorias (bebidas, refeições, ...)
#------ ######################################################
#'''

def main():
#    st.set_page_config(layout='wide')

    Interface.mainPage(version)

    if 'login' not in st.session_state:
        st.session_state['login'] = False

    if 'funcName' not in st.session_state:
        st.session_state['funcName'] = ''
    
    if 'privilege' not in st.session_state:
        st.session_state['privilege'] = ''

    if 'operation' not in st.session_state:
        st.session_state['operation'] = False

    if 'shopping_cart' not in st.session_state:
        st.session_state['shopping_cart'] = []
    
    if (not st.session_state['login']):
        button, st.session_state['privilege'], st.session_state['funcName'] = Interface.loginScreen(version)
        if(button):
#            st.success('Logged in!')
            st.toast("Logged in!")
            sleep(1.5)
            st.session_state['login'] = True

    if(st.session_state['login']):
        st.write(f'Usuário: {st.session_state['funcName']}')
        st.divider()
#        st.toast("Logged in!")
#        sleep(0.5)
#        st.Page(Interface.menuBar(version, st.session_state['funcName'], st.session_state['privilege']), title='Página principal')
        if(st.session_state['privilege'] == 'adm'):
            pages = [
                st.Page('interface/menu_principal.py', title='Página principal - Cardápio'),
                st.Page('interface/realizar_venda.py', title='Realizar Venda'),
                st.Page('interface/listar_vendas.py', title='Listar Vendas'),
                st.Page('interface/cadastrar_produto.py', title='Cadastrar Produtos'),
                st.Page('interface/cadastrar_categoria.py', title='Cadastrar Categorias'),
                st.Page('interface/excluir_produto.py', title='Excluir Produtos'),
                st.Page('interface/excluir_categoria.py', title='Excluir Categorias'),
#                st.Page('interface/logoff.py', title='Logoff')
            ]

        else:
            pages = [
                st.Page('interface/menu_principal.py', title='Página principal'),
                st.Page('interface/realizar_venda.py', title='Realizar Venda'),
                st.Page('interface/listar_vendas.py', title='Listar Vendas')
#                st.Page('interface/logoff.py', title='Logoff')
            ]

        pg = st.navigation(pages)
        pg.run()
#            Interface.tabs(funcName)

def main2():
    loggedIn = False
    while(not loggedIn):
        print(Interface.loginScreen(version))
        loginUsername = Interface.askForLogin()
        loginPassword = Interface.askforPassword()
        if(not Login_manager().check(loginUsername, loginPassword)):
            print(Interface.userLogin(False))
        else:
            running = True
            loggedIn = True
            print(Interface.userLogin(True, Funcionarios().getName(loginUsername)))
            while(running):
                func_id = Funcionarios().get_func_id(loginUsername)
                print(Interface.menu(Funcionarios().getName(loginUsername)))
                inputMenu = Interface.inputMenu()

                if(inputMenu == '1'): # Realizar Venda
                    Vendas().sale(func_id)

                elif(inputMenu == '2'): # Listar Produtos
                    print('Lista de produtos disponíveis:')
                    print(Produtos())
                    input('Aperte enter para continuar...')

                elif(inputMenu == '3'): # Listar categorias
                    print('Lista de categorias disponíveis:')
                    print(Categoria())
                    input('Aperte enter para continuar...')

                elif(inputMenu == '4'): # Listar vendas por funcionários (somente com privilégios de adm)
                    if(Funcionarios().check_privileges(Funcionarios().get_func_id(loginUsername)) != 'adm'):
                        print('Você não é um ADM!')
                    else:
                        lista_de_vendas = db().listSales()
                        lista_quantidade = db().listProductQuantity()
                        lista_base = []
                        lista_carrinho = []
                        for venda in lista_de_vendas:
                            lista_base.append(venda[0:3]) # 0-> funcID; 1-> total_value; 2-> date_time
                            lista_carrinho.append(venda[3:]) # 3... -> shopping_cart
                        print(40*'*')
                        for i in range (len(lista_base)):
                            print(f'Venda realizada em {lista_base[i][2]} por {Funcionarios().getNameById(lista_base[i][0])}:')
                            lista_itens = lista_carrinho[i][0].split(',')
                            lista_itens_quantidade = lista_quantidade[i][0].split(',')
                            for j in range(len(lista_itens)):
                                print(f'\n{3*" "}{lista_itens_quantidade[j]}x {Produtos().get_product_name(int(lista_itens[j]))}')
                                print(f'{6*" "}- Preço unitário: R${Produtos().get_product_price(Produtos().get_product_name(int(lista_itens[j]))):.2f}')
                            print(f'\nValor total da venda: R${lista_base[i][1]:.2f}')
                            print(40*'*')
                        input('Aperte enter para continuar...')
                            
                elif(inputMenu == '5'): # Cadastrar produto
                    if(Funcionarios().check_privileges(Funcionarios().get_func_id(loginUsername)) != 'adm'):
                        print('Você não é um ADM!')
                    else:
                        print('Digite o nome do produto: ')
                        productName = Interface.inputMenu()
                        print('Digite o preço do produto: ')
                        productPrice = Interface.inputMenu()
                        print('Digite a categoria do produto: ')
                        productCategory = Interface.inputMenu()
                        try:
                            Produtos().add_product(productName, productPrice, productCategory)
                            print('Cadastro concluído!')
                        except:
                            print('Um erro ocorreu.')

                elif(inputMenu == '6'): # Cadastrar categoria
                    if(Funcionarios().check_privileges(Funcionarios().get_func_id(loginUsername)) != 'adm'):
                        print('Você não é um ADM!')
                    else:
                        print('Digite o nome da categoria do produto que deseja cadastrar:')
                        category_name = input('>>>> ')
                        if(not Categoria().category_exists(category_name)):
                            Categoria().add_category(category_name)
                            print('Sucesso!')
                        else: 
                            print('Algo deu errado')


                elif(inputMenu == '7'): # Cadastrar funcionários (somente com privilégios de adm)
                    if(Funcionarios().check_privileges(Funcionarios().get_func_id(loginUsername)) != 'adm'):
                        print('Você não é um ADM!')
                    else:
                        print('Digite o nome do funcionário que será cadastrado:')
                        name = Interface.inputMenu()
                        try:
                            Funcionarios().add_employee(name, name, name)
                            print('Funcionário cadastrado com sucesso.')
                            input('Aperte enter para continuar...')
                            
                        except:
                            print('Um erro ocorreu.')

                elif(inputMenu == '0'): # Logout
                    loggedIn = False
                    running = False

                elif(inputMenu == '*'): # Encerrar programa
                    running = False

                else:
                    print('Opção inválida')

if __name__ == '__main__':
    main()
