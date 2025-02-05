import sqlite3
from pprint import pprint as pp
#from funcionarios import Funcionarios
#from produtos import Produtos
#from vendas import Vendas

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
db_manager().deleteTables()
db_manager().createTables('funcionarios','(username, password, name, privilégios)')
db_manager().createTables('produtos','(product_name, price, id_categoria)')
db_manager().createTables('categorias','(categoria)')
db_manager().createTables('vendas','(produtos_id, product_quantity, final_price, id_funcionario, shopping_cart)')
'''
# -------------------------------
'''
        self.cursor.execute("""
        INSERT INTO funcionarios VALUES
                    ('maria', '12345678', 'Maria', '0'),
                    ('pedro', '12345678', 'Pedro', '0'),
                    ('joao', '12345678', 'Joao', '0')
    """)
        self.connection.commit()
    
    def productExists(fetchConsult):
        if(fetchConsult):
            return True
        else:
            return False
    
    def sale():
        productName = input('Digite o nome do produto:')
    #    consult = cursor.execute(f'SELECT ROWID, product_name, price FROM produtos WHERE product_name = "{productName}"')
    #    fetchConsult = consult.fetchall()
        if(Produtos().product_exists(productName)):
            pp(f'Produto encontrado!')
            pp(f'Informações sobre "{productName}":')
            productId = Produtos().get_product_id(productName)
            productPrice = Produtos().get_product_price(productName)
            pp(f'Id: {productId}')
            pp(f'Preço: {productPrice}')
            quantity = int(input('Informe a quantidade de produtos que serão vendidos: '))
            totalValue = quantity * productPrice
            pp(f'Valor total da venda: {totalValue}')
            Vendas().add_sale(productId, quantity, totalValue)
            pp('Venda realizada')
            for product in Produtos().productID:
                if(productId == product):
                    quantity = int(input('Digite a quantidade de produtos: '))
                    totalValue = quantity * product[2]
                    print(f'Valor total da venda: {totalValue}')

                    cursor.execute(f"""
                    INSERT INTO vendas VALUES
                                ({product[0]}, {quantity}, {totalValue})
                """)
                    connection.commit() 
                    print('Venda realizada')
                    break
                else:
                    print('Id não encontrado')
        else:
            print('Produto não encontrado')
    '''
'''
def main():
#    createTables()
#    insertValues()
#    sale()
    pass

if __name__ == '__main__':
    main()
'''