import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

datos = pd.read_csv("Transformacion_de_datos/datos_1.csv")

carrera_profesional = pd.DataFrame(datos['CARRERA_PROFESIONAL'])
carrera_profesional_2 = pd.DataFrame(datos['CARRERA_PROFESIONAL'])

#Ejemplo con LabelEncoder()
le = LabelEncoder()
carrera_profesional['CARRERA_ENCODER'] = le.fit_transform(carrera_profesional)
print(carrera_profesional)

#Ejemplo con OneHotEncoder()
ohe = OneHotEncoder(sparse_output=False)
one_hot_carrera = ohe.fit_transform(carrera_profesional_2)
df = pd.DataFrame(one_hot_carrera, columns=ohe.get_feature_names_out(['CARRERA_PROFESIONAL']))
print(df)


