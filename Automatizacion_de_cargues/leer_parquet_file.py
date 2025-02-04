import pandas as pd

parquet_file = "Automatizacion_de_cargues/datos.parquet"

datos = pd.read_parquet(parquet_file)

print(datos)