from db_manager import db_manager as db

class Funcionarios:

    def __init__(self):
        self.consult = db().selectTables('rowid, username, password, name', 'funcionarios')
        self.funcID = []
        self.username = []
        self.password = []
        self.name = []
        
        for item in self.consult:
            self.funcID.append(item[0])
            self.username.append(item[1])
            self.password.append(item[2])
            self.name.append(item[3])

    def __str__(self):
        return f'Id: {self.funcID}\nUsername: {self.username}\nPassword: {self.password}\nName: {self.name}'

    def get_func_id(self, username):
        return self.funcID[self.username.index(username)]

    def get_func_id_by_name(self, username):
        return self.funcID[self.name.index(username)]

    def getName(self, username):
        return db().cursor.execute(f'SELECT name FROM funcionarios WHERE username = "{username}"').fetchall()[0][0]
    
    def getNameById(self, id):
        return db().cursor.execute(f'SELECT name FROM funcionarios WHERE rowid = "{id}"').fetchall()[0][0]

    def add_employee(self, username, password, name, privilege='nenhum'):
        db().insertValues('funcionarios', [f'("{username}", "{password}", "{name}", "{privilege}")'])

    def check_privileges(self, funcID):
        return db().cursor.execute(f'SELECT privileges FROM funcionarios WHERE rowid = "{funcID}"').fetchall()[0][0]

    def list_funcionarios(self):
        return self.name

#Funcionarios().add_employee("adm", "adm", "adm", "adm")
#Funcionarios().add_employee("joao", "joao", "João", "nenhum")
#Funcionarios().add_employee("maria", "maria", "Maria", "nenhum")
#Funcionarios().add_employee("pedro", "pedro", "Pedro", "nenhum")