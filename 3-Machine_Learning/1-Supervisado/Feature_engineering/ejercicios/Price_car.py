
import numpy as np 
import pandas as pd 

#import matplotlib.pyplot as plt
#import seaborn as sns

from sklearn.model_selection import train_test_split

#from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#from sklearn import metrics

#from sklearn.linear_model import Ridge
#from sklearn.linear_model import Lasso

# df = pd.read_csv('/data/coches_segunda_mano.csv') # Leemos el csv
df = pd.read_csv("data/coches_segunda_mano.csv")

X = df[['year', 'kms', 'power']]
y = df['price'] 

# ----------------GENERAMOS EL MODELO DE REGRESIÓN LINEAL------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 10) 

# HAGO UNA REGRESION POLINOMICA 
poly_feats = PolynomialFeatures(degree = 3)
poly_feats.fit(X_train)
X_train_poly = poly_feats.transform(X_train)
X_test_poly = poly_feats.transform(X_test)

pol_reg = LinearRegression()
pol_reg.fit(X_train_poly, y_train)

print('VAMOS A PREDECIR EL VALOR DE TU COCHE')

 # Inputs (incluyendo marca/modelo aunque no se usen)

year = int(input("Año de fabricación: "))
kms = float(input("Kilómetros recorridos: "))
power = int(input("Potencia (CV): "))
is_professional = int(input("Es para uso profesional? (0=No, 1=Sí): "))
make = input("Marca del coche: ").strip()
model = input("Modelo del coche: ").strip()

precio_estimado = pol_reg.predict(X_test_poly)

    
# Resultado
print(f"\nPRECIO ESTIMADO: {precio_estimado[0]:,.2f}€")



