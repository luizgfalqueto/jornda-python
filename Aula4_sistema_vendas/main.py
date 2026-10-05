import streamlit as st
import pandas as pd
import plotly.express as px

sell_table = pd.read_csv('vendas.csv')

st.write('# Sistema de Vendas')

# Seção de Cadastrar Venda
st.sidebar.write('## Cadastrar Vendas')

date = st.sidebar.date_input('Data da Venda', max_value='today')
seller = st.sidebar.selectbox('Vendedor', ['Luiz', 'Izadora', 'Livia', 'Lia', 'Gustavo'])
product = st.sidebar.selectbox('Produto', ['Notebook', 'Celular', 'Fone'])
quantity = st.sidebar.number_input('Quantidade', step=1)
valor = st.sidebar.number_input('valor')
save = st.sidebar.button('Cadastrar Venda', use_container_width=True)

if save:
    new_sell = [str(date), seller, product, quantity, valor]
    last_row = len(sell_table)
    sell_table.loc[last_row] = new_sell
    sell_table.to_csv('vendas.csv', index=False)
    st.success('Vendas cadastrada com sucesso')

# Seção de Vendas Cadastradas 
st.write('## Vendas Cadastradas')
st.dataframe(sell_table)

# Seção de Dashboard
st.write('## Dashboard')

invoicing = sell_table['valor'].sum()
st.metric('Faturamento Total', f'R$ {str(invoicing).replace('.', ',')}')

graficBar = px.bar(sell_table, x='vendedor', y='valor', color='produto')
st.plotly_chart(graficBar)

graficPie = px.pie(sell_table, names='produto', values='valor', hole=.5)
st.plotly_chart(graficPie)