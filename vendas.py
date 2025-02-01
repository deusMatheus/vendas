import sqlite3

connection = sqlite3.connect('dados/database.db')
cursor = connection.cursor()

class Vendas:

    def __init__(self):
        self.consult = cursor.execute('SELECT rowid, produtos_id, product_quantity, final_price FROM funcionarios').fetchall()
        self.vendaID = []
        self.produtosID = []
        self.produtosQuantidade = []
        self.precoFinal = []
        
        for item in self.consult:
            self.vendaID.append(item[0])
            self.produtosID.append(item[1])
            self.produtosQuantidade.append(item[2])
            self.precoFinal.append(item[3])

    def add_sale(self, productID, quantity, totalValue):
        cursor.execute(f"""
            INSERT INTO vendas VALUES
                        ({productID}, {quantity}, {totalValue})
        """)
        connection.commit() 
