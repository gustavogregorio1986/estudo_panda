import pandas as pd

data = {
    'Nome': ['João', 'Maria', 'Carlos', 'Ana'],
    'Idade': [25, 30, 45, 22],
    'Salario': [2500, 3200, 4000, 2800],
    'Ativo': [True, True, False, True]
}
df = pd.DataFrame(data)
print(df)

ativos = df[df['Ativo'] == True]
print(ativos)

ativos = df[df['Ativo']]

filtro = df[(df['Salario'] > 3000) & (df['Idade'] < 40)]
print(filtro)

df['Salario_Alto'] = df['Salario'] > 3000
print(df)

quantidade_ativos = df['Ativo'].sum()
print(quantidade_ativos)

def categoria_idade(idade):
    if idade < 30:
        return 'Jovem'
    elif idade < 50:
        return 'Adulto'
    else:
        return 'Sênior'

df['Categoria_Idade'] = df['Idade'].apply(categoria_idade)
print(df)

media_salario = df.groupby('Ativo')['Salario'].mean()
print(media_salario)

ativos_sorted = df[df['Ativo']].sort_values('Salario', ascending=False)
print(ativos_sorted)

duplicados = df[df['Nome'].duplicated()]
print(duplicados)

