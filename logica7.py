import pandas as pd

# 1. Leitura do arquivo CSV
arquivo_csv = 'vendas.csv'  # Substitua pelo nome do seu arquivo
df = pd.read_csv(arquivo_csv)

# 2. Exibir as primeiras linhas do DataFrame
print("Dados originais:")
print(df.head())

# 3. Agrupar os dados por categoria e calcular a soma das vendas e a média do preço
resultado = df.groupby('Categoria').agg(
    total_vendas=('Valor', 'sum'),  # Soma dos valores das vendas por categoria
    media_preco=('Preco', 'mean')   # Média dos preços por categoria
).reset_index()

# 4. Exibir o resultado do agrupamento
print("\nResultado do agrupamento:")
print(resultado)

# 5. Salvar o resultado em um novo arquivo CSV
novo_arquivo_csv = 'vendas_agrupadas.csv'
resultado.to_csv(novo_arquivo_csv, index=False)

print(f"Arquivo salvo com sucesso: {novo_arquivo_csv}")
