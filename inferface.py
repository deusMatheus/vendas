# A classe interface, posteriormente, será transformada para utilizar o streamlit

class Interface:

    def loginScreen():
        message = 'Sistema de Vendas 0.1'
        return f'{"*"*len(message)}\n{message}\n{"*"*len(message)}'
    
    def askForLogin():
        return input('Digite seu username: ')
    
    def askforPassword():
        return input('Digite sua senha: ')
    
    def userLogin(flag):
        if(flag):
            return f'Logado!'
        else:
            return f'Usuário ou senha incorretos!'

    def menu(name):
        welcome_message = f'Bem vindo(a) {name}!'
        full_message = f'''
        Qual das opções abaixo deseja?
        1 - Realizar venda
        2 - Listar produtos
        3 - Cadastrar produto
        4 - Listar categorias
        5 - Cadastrar categoria
        * - Encerrar programa'''
        return f'{"*"*len(welcome_message)}\n{welcome_message}{full_message}\n{"*"*len(welcome_message)}'

    def inputMenu():
        return input('>>> ')