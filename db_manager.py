import sqlite3

class db_manager:

    def __init__(self):
        self.connection = sqlite3.connect('dados/database.db')
        self.cursor = self.connection.cursor()

    def getColumnsTable(self, tableName):
        return self.cursor.execute(f'PRAGMA table_info({tableName})')
        
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
        self.cursor.execute('DROP TABLE log')
        self.connection.commit()

    def selectTables(self, columns_string, table_name):
        return self.cursor.execute(f'SELECT {columns_string} FROM {table_name}').fetchall()

    def listSales(self):
        consult = self.cursor.execute(f'''
                                   SELECT id_funcionario, SUM(final_price), date_time, shopping_cart
                                   FROM vendas GROUP BY date_time
                                   HAVING count(*) >= 1 ORDER BY date_time
                                ''').fetchall()
        return consult

    def listProductQuantity(self):
        consult = self.cursor.execute(f'''
                                      SELECT group_concat(product_quantity)
                                      FROM vendas GROUP BY date_time
                                      ''').fetchall()
        return consult
    
    def resetAll(self):
        self.deleteTables()
        self.createTables('funcionarios','(username, password, name, privileges)')
        self.createTables('produtos','(product_name, price, id_categoria)')
        self.createTables('categorias','(categoria)')
        self.createTables('vendas','(produtos_id, product_quantity, final_price, id_funcionario, shopping_cart, date_time)')
        self.createTables('log', '(date, time, table, worker_id, operation_description)')
        self.insertValues('funcionarios', [f'("adm", "adm", "Administrador", "adm")'])
    
    def deleteValues(self,tableName, columnName, valueToDelete):
        self.cursor.execute(f'DELETE FROM {tableName} WHERE {columnName}={valueToDelete};')
        self.connection.commit()

# -------------------------------
# db_manager().resetAll()
# -------------------------------
