from inferface import Interface
from login_manager import Login_manager
from funcionarios import Funcionarios
from produtos import Produtos
from vendas import Vendas
from categoria import Categoria
'''
------ ######################################################
------ Sistema de Vendas 0.2.1 ------
------ Esta aplicação é um sistema de vendas, onde armazena as informações em banco de dados utilizando sqlite. 
------ Futuramente serão implementadas duas interfaces, uma para funcionários e outra para clientes.
------ Os clientes poderão visualizar os itens disponíveis como num cardápio digital, separados por categorias.
------ Inicialmente, a interface será através do terminal, mas posteriormente deve ser atualizada para utilizar o streamlit
------ ######################################################
------ Para V0.3 ------
------ Criar opção de logout e retornar para o menu de login.
------ Funcionários realizam somente vendas.
------ Funcionários com privilégios de ADM podem adicionar e excluir funcionários e produtos. Além disso, podem também listar as vendas e organizar por funcionários.
------ Documentar melhor as funções do código, especialmente a função Vendas().sale(self, funcID)
------ ######################################################
------ Concluído ------
------ Criar um sistema, utilizando DBs e funções para que através da interface seja possível adicionar e retirar itens. 
------ Criar um sistema de login e senha para funcionários
------ A tabela Funcionários deve possuir uma coluna de privilégios. Administradores recebem o privilégio adm, e funcionários não possuem privilégios. 
------ A tabela Vendas deve possuir uma coluna id_funcionário que representa o funcionário que realizou a transação
------ A tabela Produtos deve possuir uma coluna categorias (bebidas, refeições, ...)
------ ######################################################
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
