from inferface import Interface
from login_manager import Login_manager
from funcionarios import Funcionarios
from produtos import Produtos
from vendas import Vendas
'''
------ Sistema de vendas 0.1 ------
------ Criar um sistema, utilizando DBs e funções para que através da interface seja possível adicionar e retirar itens. 
------ Criar um sistema de login e senha para funcionários
------ Montar duas aplicações: uma para funcionários e outra para clientes.
------ Inicialmente, a interface será através do terminal, mas posteriormente deve ser atualizada para utilizar o streamlit
'''
'''
import streamlit as  st

st.header('Sistema de Vendas')

def main():
    
    st.image('/home/matheus/Codes/Projetos Pessoais/db_editora_ex4.svg')

    refeicoes, aperitivos, bebidas = st.tabs(['Refeições', 'Aperitivos', 'Bebidas'])

    nome = st.text_input('Nome')

    if(nome):
        st.write(f'Seu nome é {nome}')

    with refeicoes:
        col1, col2 = st.columns(2)

        with col1:
            st.image('https://sebrae.com.br/Sebrae/Portal%20Sebrae/Ideias%20de%20Negocio/Importer/Images/198_background.webp','Imagem ilustrativa', use_container_width=True)

        with col2:
            st.text('Marmita!')
            st.text('Acompanha arroz, feijão, batata frita e bife.')
            st.text('Valor: R$15,00 ')

    with aperitivos:
        pass

    with bebidas:
        pass
'''

def main():
    print(Interface.loginScreen())
    loginUsername = Interface.askForLogin()
    loginPassword = Interface.askforPassword()
    if(not Login_manager().check(loginUsername, loginPassword)):
       print(Interface.userLogin(False))
    else:
        running = True
        print(Interface.userLogin(True))
        while(running):
            print(Interface.menu(Funcionarios().getName(loginUsername)))
            inputMenu = Interface.inputMenu()

            if(inputMenu == '1'):
                Vendas().sale()

            elif(inputMenu == '2'):
                print('Lista de produtos disponíveis:')
                print(Produtos())
                input('Aperte enter para continuar...')

            elif(inputMenu == '*'):
                running = False

            elif(inputMenu == '3'):
                print('Digite o nome do produto: ')
                productName = Interface.inputMenu()
                print('Digite o preço do produto: ')
                productPrice = Interface.inputMenu()
                try:
                    Produtos().add_product(productName, productPrice)
                    print('Cadastro concluído!')
                except:
                    print('Um erro ocorreu.')
            
            else:
                print('Opção inválida')

if __name__ == '__main__':
    main()
