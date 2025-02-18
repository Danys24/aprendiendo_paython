import pyodbc as pydb
import pandas as pd

server = '74.208.120.97,11001'
db = 'TRFuentesF458'
usuario = 'usrTotalReport'
clave = 'TotalReport123'

try:
    conexion = pydb.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+';DATABASE='+db+';UID='+usuario+';PWD='+clave)
    print('Conexion exitosa')
except:
    print('Error al conectarse a la base de datos')

#Consultar en la base de datos
cursor = conexion.cursor()
#cursor.execute('SELECT TOP 100000 FechaCorte, DepositoJudicial, TipoCliente,TipoIdentificacion,NumeroIdentificacion,IdTipoPersonaJuridica,NombreRazonSocial,Nacionalidad,Moneda,SaldoMonedaOrigen,SaldoCOP,SaldoMonedaOrigenABS,SaldoCOPABS,IdTipoSegmentacion,IdTipoSegmentacionMoneda,IdAnioMes FROM dbo.DetalleCargue;')

#clientes = cursor.fetchone() #fetchone trae los registros de la tabla uno a uno

#while clientes:
    #print(clientes)
    #clientes = cursor.fetchone() 

#clientes = cursor.fetchall() #fetchone trae todos los registros de la tabla
#print(clientes)

#for index in clientes:
#    print(index)

# visualizar los registros de la tabla mediante pandas
consulta = 'SELECT TOP 100000 FechaCorte, DepositoJudicial, TipoCliente,TipoIdentificacion,NumeroIdentificacion,IdTipoPersonaJuridica,NombreRazonSocial,Nacionalidad,Moneda,SaldoMonedaOrigen,SaldoCOP,SaldoMonedaOrigenABS,SaldoCOPABS,IdTipoSegmentacion,IdTipoSegmentacionMoneda,IdAnioMes FROM dbo.DetalleCargue'
datos = pd.read_sql_query(consulta,conexion)
datos['IdAnioMes'] = datos['IdAnioMes'].astype(str).str.slice(start=4)
#datos['IdAnioMes'] = datos['IdAnioMes'][3:]
print(datos)


#Descomentar para crear un excel de la data obtenida de la base de datos
#datos.to_excel('Semana_5_Automatizacion_de_cargues/458.xlsx', index=None, header=True)

cursor.close()
conexion.close()