# PREDICCIÓN DE LA ALTURA SEGUN TU EDAD

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import pickle

#LO PUSE DE PRIMERAS PARA ELIMINAR EL WARNING QUE ME SALIA AL METER LA EDAD, PERO LO HE ARREGLADO AL FINAL
#import warnings
#warnings.filterwarnings('ignore')

lista_alumnos = [("Leonardo S", 24, 1.82), 
                 ("Piero T", 25, 1.71), 
                 ("Marta B", 35, 1.66), 
                 ("Silvia P", 37, 1.63), 
                 ("Faro Z", 29, 1.90), 
                 ("Miguel N", 27, 1.80), 
                 ("Alejandro M", 28, 1.70), 
                 ("Cristina M", 32, 1.60), 
                 ("Francisco P", 36, 1.74), 
                 ("Jorge D", 45, 1.72), 
                 ("Jesús L", 41, 1.65), 
                 ("Marta G", 30, 1.65), 
                 ("Jennifer S", 40, 1.60), 
                 ("Diego I", 39, 1.80), 
                 ("Antonio C", 23, 1.77), 
                 ("Juan M", 32, 1.75), 
                 ("David S", 27, 1.70), 
                 ("Antonio J", 34, 1.80), 
                 ("Carlos H", 27, 1.77), 
                 ("Erik U", 28, 1.70), 
                 ("Marcos L", 35, 1.80)] 

df_alumnos = pd.DataFrame(lista_alumnos, columns=["Nombre", "Edad", "Altura"]) # Creamos el DataFrame

df_alumnos.to_csv('alturas.csv')

'''
X = df_alumnos[['Edad']]
y = df_alumnos['Altura']      

# ----------------GENERAMOS EL MODELO DE REGRESIÓN LINEAL------------------------

lm = LinearRegression()
lm.fit(X, y)

with open('3_1 Height.pkl', 'wb') as f:
    pickle.dump(lm, f)
    
'''



