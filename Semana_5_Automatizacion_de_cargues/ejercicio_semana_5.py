import os
import pandas as pd

# Directorio con los archivos
folder_path = "Automatizacion_de_cargues/"  # Cambia a la ruta donde están tus archivos

# Crear una lista para almacenar los DataFrames
data = []

# Iterar sobre los archivos en la carpeta
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):  # Filtra solo los archivos .csv
        df = pd.read_csv(os.path.join(folder_path, file_name))
        data.append(df)        
    elif file_name.endswith(".xlsx"):
        df = pd.read_excel(os.path.join(folder_path, file_name))
        data.append(df)

# Consolidar todos los DataFrames en uno solo
combined_df = pd.concat(data, ignore_index=True)

# Guardar en un archivo Excel
output_file = "Automatizacion_de_cargues/data_consolidada.xlsx"
combined_df.to_excel(output_file, index=False)

print(f"Archivos combinados y guardados en {output_file}")