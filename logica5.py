import pandas as pd

# Dados de exemplo
dados_vendas = {
    'Data': ['2024-12-01', '2024-12-01', '2024-12-02', '2024-12-02', '2024-12-03', '2024-12-03', '2024-12-04'],
    'Produto': ['Camiseta', 'Calça', 'Camiseta', 'Jaqueta', 'Calça', 'Tênis', 'Tênis'],
    'Quantidade': [10, 5, 15, 2, 10, 8, 12],
    'Preco_Unitario': [50, 100, 50, 200, 100, 150, 150]
}

df = pd.DataFrame(dados_vendas)
df['Data'] = pd.to_datetime(df['Data'])  # Convertendo para tipo datetime
print(df)

faturamento_diario = df.groupby('Data')['Valor_Total'].sum()
print(faturamento_diario)

produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().idxmax()
print(f"Produto mais vendido: {produto_mais_vendido}")

dia_maior_faturamento = faturamento_diario.idxmax()
maior_faturamento = faturamento_diario.max()
print(f"Dia com maior faturamento: {dia_maior_faturamento} (R$ {maior_faturamento:.2f})")

media_faturamento = faturamento_diario.mean()
print(f"Média de faturamento diário: R$ {media_faturamento:.2f}")

receita_por_produto = df.groupby('Produto')['Valor_Total'].sum()
produtos_acima_mil = receita_por_produto[receita_por_produto > 1000]
print(produtos_acima_mil)
