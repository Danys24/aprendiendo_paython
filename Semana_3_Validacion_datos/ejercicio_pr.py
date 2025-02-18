import pandas as pd
import logging
import os

# Configuración básica de logging
LOG_FILE = 'error_log.log'

# Asegurarse de limpiar el archivo de log al iniciar (opcional)
if os.path.exists(LOG_FILE):
    open(LOG_FILE, 'w').close()  # Limpia el archivo existente

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Función para validar datos
def validate_data(df):
    invalid_rows = df[df['edad'] < 0]  # Identificar datos inválidos
    if not invalid_rows.empty:
        for index, row in invalid_rows.iterrows():
            logging.error(f"Fila inválida en el índice {index}: {row.to_dict()}")
    return invalid_rows

# Simular datos
data = {
    'nombre': ['Alice', 'Bob', 'Charlie'],
    'edad': [25, -5, 30]  # Dato inválido: -5
}

df = pd.DataFrame(data)

# Validar y exportar datos inválidos
invalid_data = validate_data(df)
if not invalid_data.empty:
    invalid_data.to_csv('invalid_data.csv', index=False)
    print("Datos inválidos exportados a 'invalid_data.csv'")
else:
    print("Todos los datos son válidos.")

# Confirmar si el archivo de log se generó
if os.path.exists(LOG_FILE):
    print(f"Los errores se registraron correctamente en '{LOG_FILE}'")
else:
    print("No se generó el archivo de log. Revisa la configuración.")
