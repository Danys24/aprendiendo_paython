import pandas as pd

parquet_file = "Semana_5_Automatizacion_de_cargues/datos.parquet"

datos = pd.read_parquet(parquet_file)

print(datos)