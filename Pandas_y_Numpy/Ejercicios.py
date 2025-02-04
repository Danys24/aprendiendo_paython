import pandas as pd

naranjas = pd.Series([4,9,2,6,10,200])
#print(naranjas)

materias = pd.Series({'Lengua':5,'Ingles':4,'Matematicas':4})
#print(materias)
#print(materias[['Lengua','Ingles']])
#print(materias[materias > 4])

numeros = pd.Series([1,4,5,6,7])

#print(numeros.index)
#print(numeros.dtype)
#print(numeros.size)

data = 7

series = pd.Series(data, index=[0,1,2,3])
#print(series)

data_list = ['USD','COP','EUR']
indices = ['Dolar','Peso Colombiano', 'Euro']
monedas = pd.Series(index=indices,data=data_list)
print(monedas)