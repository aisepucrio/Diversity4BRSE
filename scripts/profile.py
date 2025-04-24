import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

def split_discriminacoes(texto):
    if not isinstance(texto, str):
        return []
    return re.split(r',\s(?=\w+\s?\()', texto)

df = pd.read_csv("analise_i&d_up.csv")

col_senioridade = "Por favor indique a senioridade do posição que ocupa.  "
col_raca = "Como voce se autodeclara?"
col_pcd = "Você é uma pessoa com deficiência? "
col_genero = "Como você se identifica em relação à sua identidade de gênero?"
col_sex = "Como você se identifica em relação à sua orientação sexual?  "
col_discriminacao = "Qual(is) dos tipos de discriminação você acha que são mais recorrentes dentro da área de desenvolvimento de software?"

df = df[[col_genero, col_sex, col_raca, col_pcd, col_senioridade,col_discriminacao]].dropna()
df[col_discriminacao] = df[col_discriminacao].apply(split_discriminacoes)
df = df.explode(col_discriminacao)
df[col_discriminacao] = df[col_discriminacao].str.strip()

mapa_genero = {
    "homem cisgênero": "Men",
    "homem trans": "Men",
    "mulher cisgênero": "Women",
    "mulher trans": "Women",
    # "não-binário": "Others G",
    # "bigênero": "Others G",
    # "prefiro não responder": "Others G",
    # "não sei": "Others G",
    # "outro": "Others G"
}

def mapear_genero(val):
    if not isinstance(val, str):
        return 
    val = val.strip().lower()
    return mapa_genero.get(val)

df["Gênero Agrupado"] = df[col_genero].apply(mapear_genero)

mapa_sexualidade = {
    "heterossexual": "Heterosexual",
    "homossexual": "LGBTQ+",
    "bissexual": "LGBTQ+",
    "pansexual": "LGBTQ+",
    # "prefiro não responder": "Others S",
    # "outro": "Others S",
    # "não sei": "Others S"
}

def mapear_sexualidade(val):
    if not isinstance(val, str):
        return
    val = val.strip().lower()
    return mapa_sexualidade.get(val)

df["Sexualidade Agrupada"] = df[col_sex].apply(mapear_sexualidade)

def mapear_pcd(val):
    if not isinstance(val, str):
        return
    val = val.strip().lower()
    if val.startswith("sim"):
        return "Disabled"
    elif "não" in val:
        return "Not disabled"
    else:
        return "Disabled"

df["PCD"] = df[col_pcd].apply(mapear_pcd)

mapa_raca = {
    "preto(a)": "PoC",
    "branco(a)": "White",
    "pardo(a)": "PoC",
    "indígena": "PoC",
    # "prefiro não responder": "Others R",
    # "outro": "Others R"
}

def mapear_raca(val):
    if not isinstance(val, str):
        return
    val = val.strip().lower()
    return mapa_raca.get(val)

df["Raça Agrupada"] = df[col_raca].apply(mapear_raca)

mapa_senioridade = {
    "estagiário": "Intern",
    "júnior (até 5 anos)": "Junior",
    "pleno (6 a 9 anos)": "Mid-level",
    "sênior (10+ anos)": "Senior"
}

def mapear_senioridade(val):
    if not isinstance(val, str):
        return
    val = val.strip().lower()
    return mapa_senioridade.get(val)

df["Senioridade Agrupada"] = df[col_senioridade].apply(mapear_senioridade)

tipos_validos = [
    "Etarismo", "Machismo", "Homofobia",
    "Racismo", "Elitismo", "Capacitismo"
]

tipos_traduzidos = {
    "Etarismo": "Ageism",
    "Machismo": "Sexism",
    "Homofobia": "Homophobia",
    "Racismo": "Racism",
    "Elitismo": "Elitism",
    "Capacitismo": "Ableism"
}

def mapear_discriminacao(val):
    if not isinstance(val, str):
        return
    val = val.strip()
    tipo = val.split("(")[0].strip()
    return tipos_traduzidos.get(tipo)

df["Discriminação Label"] = df[col_discriminacao].apply(mapear_discriminacao)

df_genero = df.rename(columns={"Gênero Agrupado": "Perfil"})[["Perfil", "Discriminação Label"]]
df_pcd = df.rename(columns={"PCD": "Perfil"})[["Perfil", "Discriminação Label"]]
df_sexualidade = df.rename(columns={"Sexualidade Agrupada": "Perfil"})[["Perfil", "Discriminação Label"]]
df_raca = df.rename(columns={"Raça Agrupada": "Perfil"})[["Perfil", "Discriminação Label"]]
df_senioridade = df.rename(columns={"Senioridade Agrupada": "Perfil"})[["Perfil", "Discriminação Label"]]
df_total = df.copy()
df_total["Perfil"] = "Total (overall)"

df_final = pd.concat([
    df_genero,
    df_sexualidade,
    df_raca,
    df_senioridade,
    df_pcd,
    df_total[["Perfil", "Discriminação Label"]]
], ignore_index=True)

df_resp = pd.read_csv("analise_i&d_up.csv")
df_resp["Gênero Agrupado"] = df_resp[col_genero].apply(mapear_genero)
df_resp["Sexualidade Agrupada"] = df_resp[col_sex].apply(mapear_sexualidade)
df_resp["Raça Agrupada"] = df_resp[col_raca].apply(mapear_raca)
df_resp["Senioridade Agrupada"] = df_resp[col_senioridade].apply(mapear_senioridade)
df_resp["PCD"] = df_resp[col_pcd].apply(mapear_pcd)

total_por_perfil = {}
for g in df_resp["Gênero Agrupado"].unique():
    total_por_perfil[g] = len(df_resp[df_resp["Gênero Agrupado"] == g])
for s in df_resp["Sexualidade Agrupada"].unique():
    total_por_perfil[s] = len(df_resp[df_resp["Sexualidade Agrupada"] == s])
for r in df_resp["Raça Agrupada"].unique():
    total_por_perfil[r] = len(df_resp[df_resp["Raça Agrupada"] == r])
for s in df_resp["Senioridade Agrupada"].unique():
    total_por_perfil[s] = len(df_resp[df_resp["Senioridade Agrupada"] == s])
for d in df_resp["PCD"].unique():
    total_por_perfil[d] = len(df_resp[df_resp["PCD"] == d])
total_por_perfil["Total (overall)"] = len(df_resp)

counts = df_final.groupby(["Perfil", "Discriminação Label"]).size().reset_index(name="count")
counts["percent"] = counts.apply(
    lambda row: (row["count"] / total_por_perfil.get(row["Perfil"], 1)) * 100,
    axis=1
)

#ordem_discriminacao = ["Sexism", "Elitism", "Ableism", "Homophobia", "Ageism", "Racism", "Others"]
#ordem_discriminacao = ["Racism", "Homophobia", "Ageism", "Ableism", "Elitism", "Sexism", "Others"]
ordem_discriminacao = ["Ableism", "Ageism", "Elitism", "Homophobia", "Racism", "Sexism"]
heatmap_data = counts.pivot_table(
    index="Perfil",
    columns="Discriminação Label",
    values="percent",
    fill_value=0
)

heatmap_data = heatmap_data[ordem_discriminacao]

ordem_perfis = [
    "Women", "Men",  # Gênero
    "Heterosexual", "LGBTQ+",  # Sexualidade
    "White", "PoC",  # Raça
    "Intern", "Junior", "Mid-level", "Senior",  # Senioridade
    "Not disabled", "Disabled",
    "Total (overall)"  # Total geral
]

heatmap_data = heatmap_data.reindex(ordem_perfis)

plt.figure(figsize=(4,4))
sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".1f",
    cmap="Reds",
    linewidths=.5,
    annot_kws={'size': 14},
    cbar_kws={'label': '% of respondents'}
)

for index, row in heatmap_data.iterrows():
    for column in heatmap_data.columns:
        print(f"Value at ({index}, {column}): {row[column]:.1f}%")   

# plt.xlabel("Type of Discrimination")
# plt.ylabel("Profile")
plt.xticks(rotation=0, ha='center', fontsize=12)
plt.yticks(rotation=0, fontsize=12)
plt.tight_layout()
#plt.title("Perception of Discrimination by Gender and Sexuality", fontsize=14, weight='bold')
plt.show()