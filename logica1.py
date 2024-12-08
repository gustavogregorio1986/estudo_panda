import pandas as pd

# Dados de exemplo
dados = {
    'Data': ['2024-12-01', '2024-12-02', '2024-12-02', '2024-12-03', '2024-12-03', '2024-12-04', '2024-12-05'],
    'Tipo': ['Crédito', 'Débito', 'Débito', 'Crédito', 'Débito', 'Débito', 'Crédito'],
    'Valor': [2000, -500, -200, 1500, -1000, -700, 3000],
    'Categoria': ['Salário', 'Mercado', 'Transporte', 'Venda', 'Lazer', 'Saúde', 'Investimento']
}

df = pd.DataFrame(dados)
df['Data'] = pd.to_datetime(df['Data'])  # Convertendo a coluna Data para o formato de data
print(df)

df['Saldo_Acumulado'] = df['Valor'].cumsum()
print(df)

transacoes_altas = df[abs(df['Valor']) > 1000]
print(transacoes_altas)

gastos_por_categoria = df[df['Tipo'] == 'Débito'].groupby('Categoria')['Valor'].sum()
print(gastos_por_categoria)

categoria_mais_gasto = gastos_por_categoria.idxmin()
valor_mais_gasto = gastos_por_categoria.min()
print(f"A categoria com maior gasto foi {categoria_mais_gasto} com um total de R$ {abs(valor_mais_gasto):.2f}.")

transacoes_credito = df[df['Tipo'] == 'Crédito']
print(transacoes_credito)

saldo_diario = df.groupby('Data')['Valor'].sum().cumsum()
print(saldo_diario)

transacoes_ordenadas = df.sort_values('Valor', ascending=False)
print(transacoes_ordenadas)

debito_por_dia = df[df['Tipo'] == 'Débito'].groupby('Data')['Valor'].sum()
dia_maior_debito = debito_por_dia.idxmin()
valor_maior_debito = debito_por_dia.min()
print(f"O maior débito ocorreu em {dia_maior_debito.date()} com um total de R$ {abs(valor_maior_debito):.2f}.")
