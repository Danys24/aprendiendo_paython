import pandas as pd

csv_file = "Automatizacion_de_cargues/datos_2.csv"
parquet_file = "Automatizacion_de_cargues/datos.parquet"

datos = pd.read_csv(csv_file)

datos.to_parquet(parquet_file,  engine="fastparquet")
