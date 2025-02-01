import sqlite3

connection = sqlite3.connect('dados/database.db')
cursor = connection.cursor()

class Funcionarios:

    def __init__(self):
        self.consult = cursor.execute('SELECT rowid, username, password, name FROM funcionarios').fetchall()
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
        return f'Username: {self.username}\nPassword: {self.password}\nName: {self.name}'
