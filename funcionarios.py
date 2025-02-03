import sqlite3
from db_manager import db_manager as db

#connection = sqlite3.connect('dados/database.db')
#cursor = connection.cursor()

class Funcionarios:

    def __init__(self):
        self.consult = db().cursor.execute('SELECT rowid, username, password, name FROM funcionarios').fetchall()
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

    def getName(self, username):
        return db().cursor.execute(f'SELECT name FROM funcionarios WHERE username = "{username}"').fetchall()[0][0]

    def add_employee(self, username, password, name):
        db().cursor.execute(f"""
            INSERT INTO funcionarios VALUES
                        ("{username}", "{password}", "{name}", 0) 
        """) # Futuramente, o 0 precisa sair
        db().connection.commit()
