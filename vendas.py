from db_manager import db_manager as db
from produtos import Produtos 
from pprint import pprint as pp
from funcionarios import Funcionarios
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
        db().insertValues('vendas', [f'({int(productID)}, {int(quantity)}, {float(totalValue)}, {funcID}, "{shoppingCart}", "{sale_date}")'])

    def list_sales(self):
        sales_dict = {}
        sales = db().listSales()
        quantity = db().listProductQuantity()
        base_list = []
        shopping_list = []
        for sale in sales:
            base_list.append(sale[0:3]) # 0-> funcID; 1-> total_value; 2-> date_time
            shopping_list.append(sale[3:]) # 3... -> shopping_cart

        for i in range(len(base_list)):
            func_name = Funcionarios().getNameById(base_list[i][0])
            sale_date = base_list[i][2]
            itens_list = shopping_list[i][0].split(',')
            quantity_list = quantity[i][0].split(',')
            itens_temp = []
            for j in range(len(itens_list)):
                itens_temp.append(f'{quantity_list[j]}x {Produtos().get_product_name(int(itens_list[j]))} - R${Produtos().get_product_price(Produtos().get_product_name(int(itens_list[j]))):.2f}')
                sale_value = f'R${base_list[i][1]:.2f}'
                sales_dict[sale_date] = [func_name]
                sales_dict[sale_date].append(itens_temp)
                sales_dict[sale_date].append(sale_value)
#                print('\n-----')
#                print(f'{func_name}')
#                print(f'{sale_date}')
#                print(f'{quantity_list[j]}x {Produtos().get_product_name(int(itens_list[j]))}')
#                print(f'Preço unitário: R${Produtos().get_product_price(Produtos().get_product_name(int(itens_list[j]))):.2f}')
#                print(f'Valor total da venda: R${base_list[i][1]:.2f}')
#                print('-----')
#        print(sales_dict)
        return sales_dict

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

