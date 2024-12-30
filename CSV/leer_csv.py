import csv

archivo_csv = 'CSV/F211PRU.csv'

try:    
    with open(archivo_csv, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            print("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])) 

except FileNotFoundError:
    print(f"El archivo {archivo_csv} no existe.")

except IndexError:
    print("Se intentó acceder a una columna que no existe.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

