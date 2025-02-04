import sqlite3

connection = sqlite3.connect('dados/database.db')
cursor = connection.cursor()

class Produtos:

    def __init__(self):
        self.consult = cursor.execute('SELECT rowid, product_name, price FROM produtos').fetchall()
        self.productID = []
        self.productName = []
        self.price = []
        for item in self.consult:
            self.productID.append(item[0])
            self.productName.append(item[1])
            self.price.append(item[2])

    def __str__(self):
        return f'Id: {self.productID}\nproductName: {self.productName}\nPrice: {self.price}\n'
    
    def product_exists(self, productName):
        return True if productName in self.productName else False
    
    def get_product_id(self, productName):
        if(self.product_exists(productName)):
            return self.productID[self.productName.index(productName)]

    def get_product_price(self, productName):
            if(self.product_exists(productName)):
                return self.price[self.productName.index(productName)]
            
    def get_product_name(self, productId):
            tempProductName = self.productName[self.productID.index(productId)]
            if(self.product_exists(tempProductName)):
                return tempProductName
            
    def add_product(self, productName, productPrice):
        cursor.execute(f"""
            INSERT INTO produtos VALUES
                        ("{productName}", "{productPrice}")
        """)
        connection.commit()
