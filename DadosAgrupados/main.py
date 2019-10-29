import math
import pandas as pd

pd.options.display.max_rows = 10
data  = pd.read_csv("untitled.csv")
print(data)

desvioporgrupo = data.groupby(["animal"]).agg({"water_need": ["std"]})
print(desvioporgrupo)

desvio = data.water_need.std()
print(format(desvio))

media = data.water_need.mean()
print(format(media))

dispersao = data.water_need.skew()
print(dispersao)

soma = data.water_need.sum()
print(soma)