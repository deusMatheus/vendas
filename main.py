from inferface import Interface
from login_manager import Login_manager
from funcionarios import Funcionarios
from produtos import Produtos
from vendas import Vendas
from categoria import Categoria
'''
------ Sistema de Vendas 0.1 ------
------ Criar um sistema, utilizando DBs e funções para que através da interface seja possível adicionar e retirar itens. 
------ Criar um sistema de login e senha para funcionários
------ Montar duas aplicações: uma para funcionários e outra para clientes.
------ Inicialmente, a interface será através do terminal, mas posteriormente deve ser atualizada para utilizar o streamlit
------ A tabela Funcionários deve possuir uma coluna de privilégios e funcionários não possuem privilégios. 
------ A tabela Vendas deve possuir uma coluna id_funcionário que representa o funcionário que realizou a transação
------ A tabela Produtos deve possuir uma coluna categorias (bebidas, refeições, ...)
------ Quando as alterações acima forem realizadas no db e no script, dar merge com a branch master e começar a chamar de V0.2
------ Para V0.2 ------
------ Criar opção de logout e retornar para o menu de login.
------ Funcionários realizam somente vendas.
------ Funcionários com privilégios de ADM podem adicionar e excluir funcionários e produtos. Além disso, podem também listar as vendas e organizar por funcionários.
------ 
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
            func_id = Funcionarios().get_func_id(loginUsername)
            print(Interface.menu(Funcionarios().getName(loginUsername)))
            inputMenu = Interface.inputMenu()

            if(inputMenu == '1'):
                Vendas().sale(func_id)

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
                print('Digite a categoria do produto: ')
                productCategory = Interface.inputMenu()
                
                try:
                    Produtos().add_product(productName, productPrice, productCategory)
                    print('Cadastro concluído!')
                except:
                    print('Um erro ocorreu.')
            
            elif(inputMenu == '4'):
                print('Lista de categorias disponíveis:')
                print(Categoria())
                input('Aperte enter para continuar...')


            elif(inputMenu == '5'):
                print('Digite o nome da categoria do produto que deseja cadastrar:')
                category_name = input('>>>> ')
                if(not Categoria().category_exists(category_name)):
                    Categoria().add_category(category_name)
                    print('Sucesso!')
                else: 
                    print('Algo deu errado')

            else:
                print('Opção inválida')

if __name__ == '__main__':
    main()
