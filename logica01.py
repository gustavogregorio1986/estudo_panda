import pandas as pd

# Dados de exemplo
estoque = {
    'Produto': ['Arroz', 'Feijão', 'Macarrão', 'Óleo', 'Sal', 'Açúcar', 'Café'],
    'Quantidade': [50, 20, 15, 5, 80, 25, 10],
    'Preço_Unitario': [5.5, 6.8, 4.2, 7.0, 2.0, 4.5, 8.5],
    'Categoria': ['Grãos', 'Grãos', 'Massas', 'Óleos', 'Temperos', 'Doces', 'Bebidas']
}

df = pd.DataFrame(estoque)
print(df)

df['Valor_Total'] = df['Quantidade'] * df['Preço_Unitario']
print(df)

baixo_estoque = df[df['Quantidade'] < 20]
print(baixo_estoque)

estoque_por_categoria = df.groupby('Categoria')['Quantidade'].sum()
print(estoque_por_categoria)

quantidade_minima = 30
df['Reabastecer'] = df['Quantidade'].apply(lambda x: max(0, quantidade_minima - x))
print(df)

valor_por_categoria = df.groupby('Categoria')['Valor_Total'].sum()
categoria_mais_valiosa = valor_por_categoria.idxmax()
valor_maior = valor_por_categoria.max()
print(f"A categoria com maior valor no estoque é {categoria_mais_valiosa}, com um total de R$ {valor_maior:.2f}.")

produtos_valor = df.sort_values('Valor_Total', ascending=False)
print(produtos_valor)

estoque_total = df['Quantidade'].sum()
df['Percentual_Estoque'] = (df['Quantidade'] / estoque_total) * 100
print(df)

reabastecimento_necessario = df[df['Reabastecer'] > 0].sort_values('Reabastecer', ascending=False)
print(reabastecimento_necessario)
