from db_manager import db_manager as db
#import sqlite3

#connection = sqlite3.connect('dados/database.db')
#cursor = connection.cursor()

class Categoria:

    def __init__(self):
        self.consult = db().selectTables('rowid, categoria', 'categorias')
        self.categoriesID = []
        self.categoriesName = []
        for item in self.consult:
            self.categoriesID.append(item[0])
            self.categoriesName.append(item[1])

    def __str__(self):
        return f'Id: {self.categoriesID}\categoryName: {self.categoriesName}\n'

    def category_exists(self, categoryName):
        return True if categoryName in self.categoriesName else False

    def get_category_id(self, categoryName):
        if(self.category_exists(categoryName)):
            return self.categoriesID[self.categoriesName.index(categoryName)]

    def add_category(self, categoryName):
        db().insertValues('categorias', [f'("{categoryName}")'])
