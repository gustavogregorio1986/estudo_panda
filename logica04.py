import pandas as pd

# Dados de exemplo
dados_estoque = {
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Impressora', 'Cadeira', 'Mesa'],
    'Categoria': ['Eletrônicos', 'Acessórios', 'Acessórios', 'Eletrônicos', 'Eletrônicos', 'Móveis', 'Móveis'],
    'Quantidade': [10, 50, 30, 15, 8, 20, 5],  # Quantidade em estoque
    'Preco_Unitario': [3000, 50, 100, 1200, 800, 350, 500]  # Preço unitário em R$
}

df = pd.DataFrame(dados_estoque)
print(df)

df['Valor_Total'] = df['Quantidade'] * df['Preco_Unitario']
print(df[['Produto', 'Valor_Total']])

produto_maior_valor = df.loc[df['Valor_Total'].idxmax()]
print(f"Produto com maior valor em estoque: {produto_maior_valor['Produto']} (R$ {produto_maior_valor['Valor_Total']:.2f})")

quantidade_total = df['Quantidade'].sum()
print(f"Quantidade total de itens em estoque: {quantidade_total}")

produtos_baixa_quantidade = df[df['Quantidade'] < 10]
print(produtos_baixa_quantidade)

valor_por_categoria = df.groupby('Categoria')['Valor_Total'].sum()
print(valor_por_categoria)

produto_mais_caro = df.loc[df['Preco_Unitario'].idxmax()]
print(f"Produto mais caro: {produto_mais_caro['Produto']} (R$ {produto_mais_caro['Preco_Unitario']:.2f})")

media_preco_por_categoria = df.groupby('Categoria')['Preco_Unitario'].mean()
print(media_preco_por_categoria)

quantidade_por_categoria = df.groupby('Categoria')['Quantidade'].sum()
print(quantidade_por_categoria)

df['Reposicao_Necessaria'] = df['Quantidade'] < 10
print(df[['Produto', 'Reposicao_Necessaria']])

produtos_ordenados = df.sort_values('Valor_Total', ascending=False)
print(produtos_ordenados[['Produto', 'Valor_Total']])

