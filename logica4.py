import pandas as pd

# Dados de exemplo
dados_vendas = {
    'Produto': ['Arroz', 'Feijão', 'Leite', 'Macarrão', 'Carne', 'Óleo', 'Pão'],
    'Categoria': ['Grãos', 'Grãos', 'Laticínios', 'Massas', 'Carnes', 'Óleos', 'Padaria'],
    'Preco': [5.0, 4.5, 3.0, 2.5, 20.0, 7.5, 1.5],  # Preço unitário em R$
    'Quantidade': [100, 200, 150, 120, 50, 80, 300],  # Quantidade vendida
    'Data_Venda': ['2024-12-01', '2024-12-01', '2024-12-02', '2024-12-02', '2024-12-03', '2024-12-04', '2024-12-05']
}

df = pd.DataFrame(dados_vendas)
df['Data_Venda'] = pd.to_datetime(df['Data_Venda'])  # Convertendo a data
print(df)

df['Receita_Total'] = df['Preco'] * df['Quantidade']
print(df[['Produto', 'Receita_Total']])

produto_mais_vendido = df.loc[df['Quantidade'].idxmax()]
print(f"Produto mais vendido: {produto_mais_vendido['Produto']} com {produto_mais_vendido['Quantidade']} unidades.")

receita_por_categoria = df.groupby('Categoria')['Receita_Total'].sum()
print(receita_por_categoria)

produtos_destaque = df[df['Receita_Total'] > 500]
print(produtos_destaque)

receita_total = df['Receita_Total'].sum()
print(f"Receita total do supermercado: R$ {receita_total:.2f}")

media_preco_por_categoria = df.groupby('Categoria')['Preco'].mean()
print(media_preco_por_categoria)

vendas_por_data = df.groupby('Data_Venda')['Quantidade'].sum()
print(vendas_por_data)

produtos_baixa_venda = df[df['Quantidade'] < 100]
print(produtos_baixa_venda)

import matplotlib.pyplot as plt

receita_por_categoria.plot(kind='bar', title='Receita por Categoria', color='skyblue')
plt.xlabel('Categoria')
plt.ylabel('Receita Total (R$)')
plt.show()

df['Percentual_Receita'] = (df['Receita_Total'] / receita_total) * 100
print(df[['Categoria', 'Receita_Total', 'Percentual_Receita']])

