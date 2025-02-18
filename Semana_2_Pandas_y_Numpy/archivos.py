import pandas as pd

df = pd.read_csv('Pandas_y_Numpy/F211PRU.csv')
df_1 = pd.read_excel('Pandas_y_Numpy/F211PRU3.xlsx')


#print(df_1['NUMERO_ID'][1])
#print(df_1)
print(df['NUMERO_ID'][1])