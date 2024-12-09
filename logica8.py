import pandas as pd
import glob

# 1. Carregar múltiplos arquivos CSV
arquivos_csv = glob.glob('vendas_*.csv')  # Todos os arquivos que começam com 'vendas_'
df_list = []

# 2. Ler e combinar os arquivos em um único DataFrame
for arquivo in arquivos_csv:
    df = pd.read_csv(arquivo)
    df_list.append(df)

# 3. Combinar todos os DataFrames em um único
dados_combinados = pd.concat(df_list, ignore_index=True)

# 4. Exibir as primeiras linhas dos dados combinados
print("Dados combinados:")
print(dados_combinados.head())

# 5. Limpeza de dados
# Remover duplicados
dados_combinados = dados_combinados.drop_duplicates()

# Tratar valores ausentes (substituindo por 0)
dados_combinados.fillna(0, inplace=True)

# Excluir colunas desnecessárias (exemplo: 'ProdutoID' se não for relevante)
dados_combinados.drop(columns=['ProdutoID'], errors='ignore', inplace=True)

# 6. Exibir os dados após limpeza
print("\nDados após limpeza:")
print(dados_combinados.head())

# 7. Salvar os dados combinados e limpos em um novo arquivo CSV
novo_arquivo_csv = 'vendas_combinadas_limpa.csv'
dados_combinados.to_csv(novo_arquivo_csv, index=False)

print(f"Arquivo salvo com sucesso: {novo_arquivo_csv}")
