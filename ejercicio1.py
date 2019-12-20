"""
    @reroes
    - uso de reduce
    -  uso de groupby
"""
from functools import reduce
from itertools import *
from collections import Counter
import pandas as pd

data = pd.read_csv("data/ods_1_2.csv")
data_record = data.to_dict("records")
print(data_record[0].keys())

lista = list(map(lambda x: x['from_user'],data_record))
print(lista)

print("--------------------------------")
# se obtiene las ocurrencias que más se repiten
lista_2 = Counter(lista).most_common(10) 
print(lista_2)

# se pasa la lista a dataFrame
data = pd.DataFrame(lista_2)

data.to_csv("data/data_user_count.csv", header=['usuario', 'numero'], index=False)
