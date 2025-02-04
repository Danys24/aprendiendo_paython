import array as ar
import numpy as np

matriz_2 = np.array([1,2,3,4])
matriz = ar.array('i',[1,2,3,4,5])
lista_1 = [1,3,6]
lista_2 = [65,90,76]
lista_3 = [10,100,988]

matriz_3 = np.array([lista_1,lista_2,lista_3])
print(matriz_3)

m = np.arange(20).reshape(2,10) #arange define la cantidad de valores y reshape el numero de filas y columnas en las cuales se van posicionar los valores

print(m)