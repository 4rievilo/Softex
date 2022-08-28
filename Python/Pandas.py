import pandas as pd

df = pd.read_csv("notas_alunos.csv")
media = (df["Nota_1"] + df["Nota_2"]) / 2
df["Media"] = media
df.loc[df["Media"] >= 7, "Situacao"] = "Aprovado"
df.loc[df["Media"] < 7, "Situacao"] = "Reprovado"
print(df)