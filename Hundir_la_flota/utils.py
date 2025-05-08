import numpy as np
import variables as vr

def crear_tablero ():
    tablero = np.full ((10,10), "_")
    return (tablero)

def colocar_barcos(tablero, lista_barcos):    

    for barco in lista_barcos:
        for i, j in barco:
            tablero[i, j] = 'O'

    return tablero

def disparo(tablero):
    fila = int(input ("Selecciona la fila"))
    columna = int(input ("Selecciona la columna"))
    
    if tablero [fila,columna] == "O":
        tablero [fila,columna] = "X"
    elif tablero [fila,columna] == "#" or tablero [fila,columna] == "X":
        print ("Disparo repetido")
    else:
        tablero [fila,columna] = "#"
    return tablero
