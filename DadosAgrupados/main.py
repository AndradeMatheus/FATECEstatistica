import math
import pandas as pd

df = pd.DataFrame(columns=["valor", "quantidade"])
n = int(input("Entre com o número de agrupamentos: "))

for _ in range(n):
    vl = input("Entre com o valor: ")
    qt = (int(input("Entre com a quantidade de valores para {}: ".format(vl))))
    df1 = pd.DataFrame(data=[[vl,qt]],columns=["valor", "quantidade"])
    df = pd.concat([df,df1], axis=0)

df.index = range(len(df.index))
print(df)

desvioporgrupo = df.groupby(["valor"]).agg({"quantidade": ["std"]})
print('Desvio por grupo: \n', desvioporgrupo)

desvio = df.quantidade.std()
print('\nDesvio: ', format(desvio))

media = df.quantidade.mean()
print('Media: ', format(media))

dispersao = df.quantidade.skew()
print('Dispersao: ', dispersao)

soma = df.quantidade.sum()
print('Soma: ', soma)