import pyodbc as pydb
import pandas as pd

server = 'LOCALHOST\SQLPRUEBA'
db = 'TotalReport'
usuario = 'total_danys'
clave = '100176'

try:
    conexion = pydb.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+';DATABASE='+db+';UID='+usuario+';PWD='+clave)
    print('Conexion exitosa')
except:
    print('Error al conectarse a la base de datos')

#Consultar en la base de datos
cursor = conexion.cursor()
cursor.execute('SELECT * FROM dbo.clientes;')

#clientes = cursor.fetchone() #fetchone trae los registros de la tabla uno a uno

#while clientes:
#    print(clientes)
#    clientes = cursor.fetchone() 

clientes = cursor.fetchall() #fetchone trae todos los registros de la tabla
#print(clientes)

for index in clientes:
    print(index)

# visualizar los registros de la tabla mediante pandas
consulta = 'SELECT * FROM dbo.clientes'
datos = pd.read_sql_query(consulta,conexion)
print(datos)


#Descomentar para crear un excel de la data obtenida de la base de datos
#datos.to_excel('Automatizacion_de_cargues/clientes.xlsx', index=None, header=True)

cursor.close()
conexion.close()