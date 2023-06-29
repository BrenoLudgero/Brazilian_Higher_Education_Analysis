import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("microdados_cadastro_IES_2021.csv", sep=";", encoding ="latin1")

cores = plt.rcParams['axes.prop_cycle'].by_key()['color']

df_regioes = df["NO_REGIAO_IES"].value_counts()
expandir = (0.06, 0, 0, 0, 0)
df_regioes.plot(kind="pie", shadow=True, title="IES por Região", explode=expandir, autopct="%1.1f%%", startangle=90)
plt.ylabel(ylabel=None)
plt.tight_layout()
plt.show()

df_estados = df["SG_UF_IES"].value_counts()[:10]
df_estados.plot(kind="barh", title="IES por Estado", width=0.7, color=cores, edgecolor="black")
plt.grid(True, axis="x", alpha=0.5)
plt.ylabel(ylabel=None)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

def df_categoria_labels(df):
    labels = []
    for i in range(len(df)):
        if (df.index[i] == 1):
            labels.append("Pública Federal")
        elif (df.index[i] == 2):
            labels.append("Pública Estadual")
        elif (df.index[i] == 3):
            labels.append("Pública Municipal")
        elif (df.index[i] == 4):
            labels.append("Privada com Fins")
        elif (df.index[i] == 5):
            labels.append("Privada sem Fins")
        else:
            labels.append("Especial")
    return labels
df_categoria = df["TP_CATEGORIA_ADMINISTRATIVA"].value_counts()
labels = df_categoria_labels(df_categoria)
expandir = (0.06, 0, 0, 0, 0, 0)
df_categoria.plot(kind="pie", shadow=True, title="IES por Categoria", explode=expandir, labels=labels, autopct="%1.1f%%", pctdistance=0.85, startangle=180, textprops={'fontsize': 9})
plt.ylabel(ylabel=None)
plt.tight_layout()
plt.show()

def org_acad_labels(df):
    labels = []
    for i in range(len(df)):
        if (df.index[i] == 1):
            labels.append("Faculdade")
        elif (df.index[i] == 2):
            labels.append("Centro Universitário")
        elif (df.index[i] == 3):
            labels.append("Universidade")
        else:
            labels.append("Instituto Federal")
    return labels
df_org_acad = df["TP_ORGANIZACAO_ACADEMICA"]
df_org_acad = df_org_acad[df_org_acad != 5].value_counts()
labels = org_acad_labels(df_org_acad)
expandir = (0.08, 0, 0, 0)
df_org_acad.plot(kind="pie", shadow=True, title="IES por Organização", explode=expandir, wedgeprops=dict(width=0.5), labels=labels, autopct="%1.0f%%", pctdistance=0.85, startangle=180)
plt.ylabel(ylabel=None)
plt.tight_layout()
plt.show()

docentes_masc = df["QT_DOC_EX_MASC"].sum()
docentes_femi = df["QT_DOC_EX_FEMI"].sum()
plt.bar("Masculino", docentes_masc, width=0.45, edgecolor="black")
plt.bar("Feminino", docentes_femi, width=0.45, edgecolor="black")
plt.title("Docentes por Sexo")
plt.grid(True, axis="y", alpha=0.5)
plt.margins(x=0.2)
plt.tight_layout()
plt.show()

docentes_dout = df["QT_DOC_EX_DOUT"].sum()
docentes_mest = df["QT_DOC_EX_MEST"].sum()
docentes_espec = df["QT_DOC_EX_ESP"].sum()
docentes_grad = df["QT_DOC_EX_GRAD"].sum()
docentes_sem_grad = df["QT_DOC_EX_SEM_GRAD"].sum()
plt.bar("Doutorado", docentes_dout, width=0.82, edgecolor="black")
plt.bar("Mestrado", docentes_mest, width=0.82, edgecolor="black")
plt.bar("Especialização", docentes_espec, width=0.82, edgecolor="black")
plt.bar("Graduação", docentes_grad, width=0.82, edgecolor="black")
plt.bar("Sem Graduação", docentes_sem_grad, width=0.82, edgecolor="black")
plt.title("Docentes por Titulação")
plt.grid(True, axis="y", alpha=0.5)
plt.tight_layout()
plt.show()

labels = ["Tempo Integral", "Tempo Parcial", "Horista"]
docentes_int = df["QT_DOC_EX_INT"].sum()
docentes_parc = df["QT_DOC_EX_PARC"].sum()
docentes_hor = df["QT_DOC_EX_HOR"].sum()
valores = [docentes_int, docentes_parc, docentes_hor]
fig, ax = plt.subplots()
expandir = (0.08, 0, 0)
ax.pie(valores, shadow=True, explode=expandir, wedgeprops=dict(width=0.5), labels=labels, autopct='%1.1f%%', pctdistance=0.75, startangle=90)
plt.title("Docentes por Regime")
plt.tight_layout()
plt.show()

labels = ["Até 29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60+"]
docentes_ate_29 = df["QT_DOC_EX_0_29"].sum()
docentes_ate_34 = df["QT_DOC_EX_30_34"].sum()
docentes_ate_39 = df["QT_DOC_EX_35_39"].sum()
docentes_ate_44 = df["QT_DOC_EX_40_44"].sum()
docentes_ate_49 = df["QT_DOC_EX_45_49"].sum()
docentes_ate_54 = df["QT_DOC_EX_50_54"].sum()
docentes_ate_59 = df["QT_DOC_EX_55_59"].sum()
docentes_mais_60 = df["QT_DOC_EX_60_MAIS"].sum()
valores = [docentes_ate_29, docentes_ate_34, docentes_ate_39, docentes_ate_44, docentes_ate_49, docentes_ate_54, docentes_ate_59, docentes_mais_60]
fig, ax = plt.subplots()
ax.bar(labels, valores, 0.7, color=cores, edgecolor="black")
plt.title("Docentes por Idade")
plt.grid(True, axis="y", alpha=0.5)
plt.tight_layout()
plt.show()

labels = ["Branca", "Parda", "Preta", "Amarela", "Indígena"]
docentes_branca = df["QT_DOC_EX_BRANCA"].sum()
docentes_parda = df["QT_DOC_EX_PARDA"].sum()
docentes_preta = df["QT_DOC_EX_PRETA"].sum()
docentes_amarela = df["QT_DOC_EX_AMARELA"].sum()
docentes_indigena = df["QT_DOC_EX_INDIGENA"].sum()
valores = [docentes_branca, docentes_parda, docentes_preta, docentes_amarela, docentes_indigena]
fig, ax = plt.subplots()
expandir = (0.08, 0, 0, 0, 0)
ax.pie(valores, shadow=True, explode=expandir, labels=labels, autopct='%1.1f%%', pctdistance=0.75, startangle=0, textprops={'fontsize': 8})
plt.title("Docentes por Cor/Raça")
plt.tight_layout()
plt.show()
