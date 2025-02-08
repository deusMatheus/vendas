from db_manager import db_manager as db
from categoria import Categoria

class Produtos:

    def __init__(self):
        self.consult = db().selectTables('rowid, product_name, price, id_categoria', 'produtos')
        self.productID = []
        self.productName = []
        self.price = []
        self.categoryID = []
        for item in self.consult:
            self.productID.append(item[0])
            self.productName.append(item[1])
            self.price.append(item[2])
            self.categoryID.append(item[3])

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
    
    def get_product_list(self):
        product_list = [
            self.productID,
            self.productName,
            self.price,
            self.categoryID
        ] 
        return product_list
            
    def add_product(self, productName, productPrice, productCategoryName):
        productCategoryID = Categoria().get_category_id(productCategoryName)
        db().insertValues('produtos', [f'("{productName}", {productPrice}, "{productCategoryID}")'])

    def list_item_by_category(self, productCategory):
        categoryID = Categoria().get_category_id(productCategory)
        return db().cursor.execute(f'SELECT product_name, price FROM produtos WHERE id_categoria = "{categoryID}"').fetchall()