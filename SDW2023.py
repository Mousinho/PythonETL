'''Objetivo vai ser pegar essa base onde se encontra todos os tsunamis
documentados e extrair dela apenas as informações de tsunamis que tenham
causada um terremoto e tenha Ano, Mês e localidade '''

# Bibliotecas
import numpy as np
import pandas as pd
import plotly.express as px

# Extração e exploração
df = pd.read_csv('tsunamis.csv', dtype='str')

print(df.isnull().sum())
print(df.head())
print(df.shape)

# Transformação

data_Tsu = df.loc[:, ["Country", "LocationNanName",
                      "Year", "Mo", "EarthquakeNanMagnitude"]]
data_Tsu.columns = ["Country", "LocationNanName",
                    "Year", "Mo", "EarthquakeNanMagnitude"]
# Aqui copiei os valores do primeiro DataFrame para o segundo com apenas as colunas escolhidas

data_Tsu = data_Tsu[data_Tsu["EarthquakeNanMagnitude"].notna()]
data_Tsu = data_Tsu[data_Tsu["Mo"].notna()]
# Retirado os valores nulos
print(data_Tsu.isnull().sum())

data_Tsu["Country"] = data_Tsu["Country"].str.replace("Nan", " ")
data_Tsu["Location Name"] = data_Tsu["LocationNanName"].str.replace("Nan", " ")
data_Tsu["Earthquake Magnitude"] = data_Tsu["EarthquakeNanMagnitude"]
# Retirando a str Nan dos nomes compostos

for column in data_Tsu.columns:
    if data_Tsu[column].dtype == "object":
        data_Tsu[column] = data_Tsu[column].str.title()
# Criei um for para interar em todas as colunas e onde for str colocar apenas a primeira letra em maisculo

data_Tsu = data_Tsu[["Country", "Location Name",
                     "Year", "Mo", "Earthquake Magnitude"]]
# Organizando o dataframe
print(data_Tsu)

fig = px.bar(data_Tsu[0:15], y="Earthquake Magnitude",
             x="Country", title="Rank de Terremotos por País")
# fig.show()

data_Tsu.to_excel("data_Tsu.xlsx", index=False)
