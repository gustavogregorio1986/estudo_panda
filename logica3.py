import pandas as pd

# Dados de exemplo
dados_alunos = {
    'Aluno': ['Ana', 'João', 'Maria', 'Carlos', 'Bia', 'Pedro', 'Lucas'],
    'Matematica': [85, 78, 92, 65, 70, 88, 95],
    'Portugues': [88, 72, 89, 58, 76, 85, 91],
    'Ciencias': [90, 85, 94, 60, 75, 80, 88],
    'Frequencia': [95, 80, 98, 70, 85, 90, 100]  # Frequência em %
}

df = pd.DataFrame(dados_alunos)
print(df)

df['Media_Geral'] = df[['Matematica', 'Portugues', 'Ciencias']].mean(axis=1)
print(df)

alunos_baixo_desempenho = df[df['Media_Geral'] < 70]
print(alunos_baixo_desempenho)

alunos_em_risco = df[df['Frequencia'] < 75]
print(alunos_em_risco)

media_por_materia = df[['Matematica', 'Portugues', 'Ciencias']].mean()
print(media_por_materia)

melhor_aluno = df.loc[df['Media_Geral'].idxmax()]
print(f"Melhor aluno: {melhor_aluno['Aluno']} com média geral de {melhor_aluno['Media_Geral']:.2f}.")

alunos_ordenados = df.sort_values('Media_Geral', ascending=False)
print(alunos_ordenados)

aprovados = df[df['Media_Geral'] >= 70]
taxa_aprovacao = (len(aprovados) / len(df)) * 100
print(f"Taxa de aprovação: {taxa_aprovacao:.2f}%")

def classificar(media):
    if media >= 90:
        return 'A'
    elif media >= 80:
        return 'B'
    elif media >= 70:
        return 'C'
    else:
        return 'D'

df['Classificacao'] = df['Media_Geral'].apply(classificar)
print(df)

correlacao = df['Media_Geral'].corr(df['Frequencia'])
print(f"Correlação entre média geral e frequência: {correlacao:.2f}")
