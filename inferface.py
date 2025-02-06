# A classe interface, posteriormente, será transformada para utilizar o streamlit

class Interface:

    def loginScreen(version):
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

    def menu(name):
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

    def inputMenu():
        return input('>>> ')