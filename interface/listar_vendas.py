from vendas import Vendas
from funcionarios import Funcionarios
from produtos import Produtos
from categoria import Categoria
import streamlit as st

sales = Vendas().list_sales()
funcionarios = Funcionarios().list_funcionarios()

#for key, value in sales.items():
#    print(f'sales[key]: {sales[key]}')
#    print(f'key: {key}')
#    print(f'value: {value}')
    
#print(sales)
#st.write(sales)

if (st.session_state['privilege'] == 'adm'):
    tabs = st.tabs(funcionarios)
#    print(funcionarios)
    for i in range(len(funcionarios)):
        with tabs[i]:
            for key, value in sales.items():
                if(sales[key][0] == funcionarios[i]):
                    st.write(f'Data da venda: {key}')
                    for produtos in sales[key][1]:
                        st.write(produtos)
                    st.write(f'Valor total: {sales[key][2]}')
                    st.divider()
#                st.write(funcionarios[i])

else:
    for key, value in sales.items():
        if(sales[key][0] == st.session_state['funcName']):
            st.write(f'Data da venda: {key}')
            for produtos in sales[key][1]:
                st.write(produtos)
            st.write(f'Valor total: {sales[key][2]}')
            st.divider()
