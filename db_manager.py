import sqlite3

class db_manager:

    def __init__(self):
        self.connection = sqlite3.connect('dados/database.db')
        self.cursor = self.connection.cursor()

    def createTables (self, table_name, values_tuple):
        self.cursor.execute(f'CREATE TABLE {table_name} {values_tuple}')
        self.connection.commit()

    def insertValues(self, table_name, values_list):
        for value_string in values_list:
            self.cursor.execute(f"""INSERT INTO {table_name} VALUES {value_string}""")
        self.connection.commit()

    def deleteTables(self):
        self.cursor.execute('DROP TABLE funcionarios')
        self.cursor.execute('DROP TABLE produtos')
        self.cursor.execute('DROP TABLE vendas')
        self.cursor.execute('DROP TABLE categorias')
        self.connection.commit()

    def selectTables(self, columns_string, table_name):
        return self.cursor.execute(f'SELECT {columns_string} FROM {table_name}').fetchall()
    
'''
# -------------------------------
db_manager().deleteTables()
db_manager().createTables('funcionarios','(username, password, name, privilégios)')
db_manager().createTables('produtos','(product_name, price, id_categoria)')
db_manager().createTables('categorias','(categoria)')
db_manager().createTables('vendas','(produtos_id, product_quantity, final_price, id_funcionario, shopping_cart)')
# -------------------------------
'''