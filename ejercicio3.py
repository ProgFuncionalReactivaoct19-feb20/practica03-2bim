"""
    @reroes
    - uso de reduce
    -  uso de groupby
"""
from collections import Counter
import pandas as pd
import datetime

data = pd.read_csv("data/ods_1_2_modificado.csv")
data_record = data.to_dict("records")

lista = list(map(lambda x: x['time'],data_record))
print(lista)

fechas = list(map(lambda x:datetime.datetime.strptime(str(x), '%d/%m/%Y %H:%M:%S'), lista))
fechas = list(map(lambda x:x.day, fechas))

# se obtiene las ocurrencias que más se repiten
lista_2 = Counter(fechas).items() 
print(lista_2)

# se pasa la lista a dataFrame
data = pd.DataFrame(lista_2)

data.to_csv("data/data_horas.csv", header=['día', 'numero'], index=False)
