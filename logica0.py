import pandas as pd

# Dados de exemplo
data = {
    'Produto': ['Camisa', 'Calça', 'Sapato', 'Jaqueta', 'Camisa', 'Calça', 'Sapato'],
    'Vendedor': ['João', 'Maria', 'Carlos', 'Ana', 'João', 'Ana', 'Carlos'],
    'Unidades_Vendidas': [10, 5, 8, 2, 15, 3, 10],
    'Preco_Unitario': [50, 80, 120, 200, 50, 80, 120],
    'Data': ['2024-12-01', '2024-12-01', '2024-12-02', '2024-12-02', '2024-12-03', '2024-12-03', '2024-12-04']
}

df = pd.DataFrame(data)
df['Data'] = pd.to_datetime(df['Data'])  # Convertendo a coluna de data
print(df)

df['Total_Venda'] = df['Unidades_Vendidas'] * df['Preco_Unitario']
print(df)

vendas_maiores = df[df['Unidades_Vendidas'] > 10]
print(vendas_maiores)

unidades_por_produto = df.groupby('Produto')['Unidades_Vendidas'].sum()
print(unidades_por_produto)

mais_vendido = unidades_por_produto.idxmax()
quantidade = unidades_por_produto.max()
print(f"O produto mais vendido foi {mais_vendido} com {quantidade} unidades.")

vendas_dia = df[df['Data'] == '2024-12-02']
print(vendas_dia)

vendas_por_vendedor = df.groupby('Vendedor')['Total_Venda'].sum()
print(vendas_por_vendedor)

ordenado = df.sort_values('Unidades_Vendidas', ascending=False)
print(ordenado)

vendas_acima_meta = df[df['Total_Venda'] > 1000]
print(vendas_acima_meta)
