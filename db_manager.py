import sqlite3
from pprint import pprint as pp

connection = sqlite3.connect('dados/database.db')
cursor = connection.cursor()

def createTables ():
    cursor.execute('CREATE TABLE funcionarios (username, password, name, vendas_ids)')
    cursor.execute('CREATE TABLE produtos (product_name, price)')
    cursor.execute('CREATE TABLE vendas (produtos_id, product_quantity, final_price, id_funcionario)')

def insertValues():

    cursor.execute("""
    INSERT INTO produtos VALUES
                   ('Sanduíche', 17.00),
                   ('Refrigerante', 7.00),
                   ('Aperitivo', 19.00),
                   ('Refeição para daus pessoas', 36.00)
""")
    connection.commit()

    cursor.execute("""
    INSERT INTO funcionarios VALUES
                   ('maria', '12345678', 'Maria', '0'),
                   ('pedro', '12345678', 'Pedro', '0'),
                   ('joao', '12345678', 'Joao', '0')
""")
    connection.commit()

def productExists(fetchConsult):
    if(fetchConsult):
        return True
    else:
        return False

def sale():
    productName = input('Digite o nome do produto:')
    consult = cursor.execute(f'SELECT ROWID, product_name, price FROM produtos WHERE product_name = "{productName}"')
    fetchConsult = consult.fetchall()
    if(productExists(fetchConsult)):
        pp(f'Produtos disponíveis: {fetchConsult}')
        productId = int(input('Digite o id do produto: '))
        for product in fetchConsult:
            if(productId == product[0]):
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

def main():
#    createTables()
#    insertValues()
    sale()

if __name__ == '__main__':
    main()
