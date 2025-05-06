import numpy as np
import barcos


def colocar_barcos(lista_barcos):    
    tablero = np.full ((10,10), "_")
    tablero_jugador = tablero

    for barco in lista_barcos:
        for i, j in barco:
            tablero_jugador[i, j] = 'O'

    return tablero