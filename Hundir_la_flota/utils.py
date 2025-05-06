import numpy as np

def crear_tablero():
    tablero = np.full ((10,10), "_")
    return (tablero)

def colocar_barco(tablero,barco):
    for i in barco:
        tablero [i[0],i[1]] = "O"
    
    return tablero
