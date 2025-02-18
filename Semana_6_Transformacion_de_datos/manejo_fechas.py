import pandas as pd
from datetime import datetime

data = {'FECHA':['2024-12-21','2024-12-22','2024-11-21','2024-12-27','2024-12-31']}

fechas = pd.DataFrame(data)

print(fechas.dtypes)

hoy = datetime.now()
fecha_formateada = hoy.strftime("%d/%m/%Y")

fechas['FECHA'] = pd.to_datetime(fechas['FECHA']).dt.strftime("%d/%m/%Y %H:%M:%S")

print(fechas.dtypes)


#print(fechas)