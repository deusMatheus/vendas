from db_manager import db_manager as db
from produtos import Produtos 
from pprint import pprint as pp
import datetime

class Vendas:

    def __init__(self):
        self.consult = db().selectTables('rowid, produtos_id, product_quantity, final_price', 'vendas')
        self.vendaID = []
        self.produtosID = []
        self.produtosQuantidade = []
        self.precoFinal = []
        
        for item in self.consult:
            self.vendaID.append(item[0])
            self.produtosID.append(item[1])
            self.produtosQuantidade.append(item[2])
            self.precoFinal.append(item[3])

    def add_sale(self, productID, quantity, totalValue, funcID, shoppingCart, sale_date):
        db().insertValues('vendas', [f'({productID}, {quantity}, {totalValue}, {funcID}, "{shoppingCart}", "{sale_date}")'])

    def sale(self, funcID):
        shoppingCart = []
        saleValue = 0
        sale = True
        while (sale):
            productName = input('Digite o nome do produto:')
            if(Produtos().product_exists(productName)):
                pp(f'Produto encontrado!')
                pp(f'Informações sobre "{productName}":')
                productId = Produtos().get_product_id(productName)
                productPrice = float(Produtos().get_product_price(productName))
                pp(f'Preço: {productPrice}')
                quantity = int(input('Informe a quantidade de produtos que serão vendidos: '))
                totalValue = quantity * productPrice
                saleValue += totalValue
                shoppingCart.append((productId, quantity, totalValue))
                confirma = input('Deseja adicionar outro produto no carrinho? (s/n) >>>> ')
                shoppingCartIDs = ''
                if(confirma == 'n' or confirma == 'N'):
                    sale = False
                    pp(f'Itens no carrinho')
                    for item in shoppingCart:
                        shoppingCartIDs += f'{item[0]}, '
                        pp(f'Item: {Produtos().get_product_name(item[0])}')
                        pp(f'Quantidade: {item[1]}')
                        pp(f'Valor: R${item[2]:.2f}')
                        pp(f'{"-"*10}')
                    shoppingCartIDs = shoppingCartIDs[:-2]
                    pp(f'Valor total da venda: R${saleValue:.2f}')
                    pp(f'Digite CONFIRMAR para confirmar a venda.')
                    pp(f'Digite CANCELAR para cancelar a venda.')
                    confirmarCompra = input('>>>> ')
                    if(confirmarCompra == 'confirmar' or confirmarCompra == 'CONFIRMAR'):
                        sale_datetime = datetime.datetime.now()
                        formatted_sale_datetime = sale_datetime.strftime('%d/%m/%Y-%H:%M:%S')
                        for item in shoppingCart:
                            self.add_sale(item[0],item[1],item[2], funcID, shoppingCartIDs, formatted_sale_datetime)
                        pp('Venda realizada com sucesso!')
                    else:
                        pp('Venda cancelada!!!')
