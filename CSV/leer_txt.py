with open('Prueba1MILL.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()

# Mantener solo las últimas líneas (2,000,001 en adelante)
with open('Prueba1MILL.txt', 'w') as nuevo_archivo:
    nuevo_archivo.writelines(lineas[1000000:])



