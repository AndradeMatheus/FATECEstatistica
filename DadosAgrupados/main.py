import math
import pandas as pd

df = pd.DataFrame(columns=["Valor", "Quantidade"])
n = int(input("Entre com o número de agrupamentos: "))

for _ in range(n):
    vl = input("Entre com o valor: ")
    qt = input("Entre com a quantidade de valores para {}: ".format(vl))
    df1 = pd.DataFrame(data=[[vl,qt]],columns=["Valor", "Quantidade"])
    df = pd.concat([df,df1], axis=0)

df.index = range(len(df.index))
print(df)

desvioporgrupo = data.groupby(["col1"]).agg({"col2": ["std"]})
print('Desvio por grupo: \n', desvioporgrupo)

desvio = data.water_need.std()
print('\nDesvio: ', format(desvio))

media = data.water_need.mean()
print('Media: ', format(media))

dispersao = data.water_need.skew()
print('Dispersao: ', dispersao)

soma = data.water_need.sum()
print('Soma: ', soma)