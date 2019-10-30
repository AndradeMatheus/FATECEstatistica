import math
import pandas as pd

pd.options.display.max_rows = 10
data  = pd.read_csv("data.csv")
print('Dados do CSV: \n', data)

desvioporgrupo = data.groupby(["animal"]).agg({"water_need": ["std"]})
print('Desvio por grupo: \n', desvioporgrupo)

desvio = data.water_need.std()
print(format('Desvio: ', desvio))

media = data.water_need.mean()
print(format('Media: ', media))

dispersao = data.water_need.skew()
print('Dispersao: ', dispersao)

soma = data.water_need.sum()
print('Soma: ', soma)