import pandas as pd

csv_file = "Semana_5_Automatizacion_de_cargues/datos_2.csv"
parquet_file = "Semana_5_Automatizacion_de_cargues/datos.parquet"

datos = pd.read_csv(csv_file)

datos.to_parquet(parquet_file,  engine="fastparquet")
