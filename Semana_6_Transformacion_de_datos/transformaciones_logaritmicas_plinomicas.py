import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Datos de ejemplo
df = pd.DataFrame({'Valor': [1, 10, 100, 1000, 10000]})

# Transformación Logarítmica
df['Valor_Log'] = np.log(df['Valor'])

print(df)


# Crear datos de ejemplo
df_poly = pd.DataFrame({'X': np.array([1, 2, 3, 4, 5])})

# Aplicar transformación polinómica de grado 2
poly = PolynomialFeatures(degree=2, include_bias=False)
df_poly_transformed = pd.DataFrame(poly.fit_transform(df_poly), columns=['X', 'X^2'])

print(df_poly_transformed)