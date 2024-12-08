import pandas as pd

# Dados de exemplo
dados_pedidos = {
    'PedidoID': [101, 102, 103, 104, 105, 106],
    'Cliente': ['João', 'Maria', 'Carlos', 'Ana', 'João', 'Carlos'],
    'Vendedor': ['Paulo', 'Paulo', 'Luana', 'Luana', 'Paulo', 'Paulo'],
    'Valor': [500, 300, 150, 700, 400, 250],
    'Data_Pedido': ['2024-12-01', '2024-12-02', '2024-12-03', '2024-12-03', '2024-12-04', '2024-12-05'],
    'Data_Entrega': ['2024-12-05', '2024-12-04', '2024-12-06', '2024-12-06', '2024-12-10', '2024-12-08']
}

df = pd.DataFrame(dados_pedidos)
df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'])
df['Data_Entrega'] = pd.to_datetime(df['Data_Entrega'])
print(df)

vendas_por_cliente = df.groupby('Cliente')['Valor'].sum()
print(vendas_por_cliente)

hoje = pd.to_datetime('2024-12-06')  # Data de referência
df['Atrasado'] = df['Data_Entrega'] > hoje
print(df)

pedidos_atrasados = df[df['Atrasado']]
print(pedidos_atrasados)

vendas_por_vendedor = df.groupby('Vendedor')['Valor'].sum()
print(vendas_por_vendedor)

inicio = '2024-12-01'
fim = '2024-12-03'
pedidos_periodo = df[(df['Data_Pedido'] >= inicio) & (df['Data_Pedido'] <= fim)]
print(pedidos_periodo)

pedido_mais_valioso = df.loc[df['Valor'].idxmax()]
print(pedido_mais_valioso)

total_vendas = df['Valor'].sum()
df['Percentual_Cliente'] = (df['Valor'] / total_vendas) * 100
print(df[['Cliente', 'Valor', 'Percentual_Cliente']])

pedidos_pendentes = df[df['Data_Entrega'] > hoje]
print(pedidos_pendentes)

desempenho_vendedores = df.groupby('Vendedor')['Valor'].sum().sort_values(ascending=False)
print(desempenho_vendedores)

