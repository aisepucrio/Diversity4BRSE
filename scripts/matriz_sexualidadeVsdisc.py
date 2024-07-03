import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'I&D4SE.xlsx'
df = pd.read_excel(file_path, usecols=['Como você se identifica em relação à sua orientação sexual?  ', 
                                       'Qual(is) dos tipos de discriminação você acha que são mais recorrentes dentro da área de desenvolvimento de software?'])

df.columns = ['sexualidade', 'discriminacao']

df = df.dropna(subset=['sexualidade'])

df['discriminacao'] = df['discriminacao'].fillna('')

discriminacoes = ['Machismo', 'Racismo', 'Elitismo', 'Etarismo', 'Capacitismo']

for disc in discriminacoes:
    df[disc] = df['discriminacao'].apply(lambda x: 1 if isinstance(x, str) and disc.lower() in x.lower() else 0)

le = LabelEncoder()
df['sexualidade_codificado'] = le.fit_transform(df['sexualidade'])

matriz = df.groupby('sexualidade_codificado')[discriminacoes].sum().T

plt.figure(figsize=(10, 7))
sns.heatmap(matriz, annot=True, cmap='Blues', xticklabels=le.classes_, yticklabels=discriminacoes)
plt.title('Matriz de Discriminação por Orientação sexual')
plt.xlabel('Orientação sexual')
plt.ylabel('Tipo de Discriminação')
plt.show()

if __name__ == "__main__":
    pass
