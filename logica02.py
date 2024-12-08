import pandas as pd

# Dados de exemplo
dados_climaticos = {
    'Data': ['2024-12-01', '2024-12-02', '2024-12-03', '2024-12-04', '2024-12-05', '2024-12-06', '2024-12-07'],
    'Temperatura': [30, 32, 28, 27, 35, 33, 29],  # Temperatura em °C
    'Umidade': [70, 65, 80, 85, 60, 75, 90],       # Umidade relativa em %
    'Precipitacao': [0, 5, 20, 0, 0, 15, 25]       # Precipitação em mm
}

df = pd.DataFrame(dados_climaticos)
df['Data'] = pd.to_datetime(df['Data'])  # Convertendo a coluna Data para formato datetime
print(df)

media_temperatura = df['Temperatura'].mean()
media_umidade = df['Umidade'].mean()

print(f"Média de Temperatura: {media_temperatura:.2f}°C")
print(f"Média de Umidade: {media_umidade:.2f}%")

dias_chuvosos = df[df['Precipitacao'] > 0]
print(dias_chuvosos)

dia_mais_quente = df.loc[df['Temperatura'].idxmax()]
print(f"Dia mais quente: {dia_mais_quente['Data'].date()} com {dia_mais_quente['Temperatura']}°C.")

dias_baixa_umidade = df[df['Umidade'] < 65]
print(dias_baixa_umidade)

precipitacao_total = df['Precipitacao'].sum()
print(f"Precipitação total no período: {precipitacao_total} mm.")

df['Condicao'] = df['Precipitacao'].apply(lambda x: 'Chuvoso' if x > 0 else 'Seco')
print(df)

resumo_climatico = df.describe()
print(resumo_climatico)

dias_quentes = df[df['Temperatura'] > media_temperatura]
print(dias_quentes)

media_por_condicao = df.groupby('Condicao')[['Temperatura', 'Umidade']].mean()
print(media_por_condicao)

