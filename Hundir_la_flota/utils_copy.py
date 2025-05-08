import numpy as np
import variables_copy as vr
import random

# Crear tableros
def crear_tablero ():
    tablero = np.full ((10,10), "_")
    return (tablero)

# Colocar barcos del jugador (manual)
def colocar_barcos_manual(tablero):
    
    for barco, tamaño in vr.barcos.items():
        colocado = False
        while not colocado:
            try:
                print(f"\nColoca tu {barco} (tamaño {tamaño})")
                fila = int(input("Fila inicial (0-9): "))
                columna = int(input("Columna inicial (0-9): "))
                orientacion = input("Orientación (H para horizontal, V para vertical): ").upper()

                if orientacion == "H":
                    if columna + tamaño > 10:
                        print("¡No cabe horizontalmente!")
                        continue
                    if any(tablero[fila, columna+i] == "O" for i in range(tamaño)):
                        print("¡Espacio ocupado!")
                        continue
                    for i in range(tamaño):
                        tablero[fila, columna+i] = "O"
                    colocado = True
                elif orientacion == "V":
                    if fila + tamaño > 10:
                        print("¡No cabe verticalmente!")
                        continue
                    if any(tablero[fila+i, columna] == "O" for i in range(tamaño)):
                        print("¡Espacio ocupado!")
                        continue
                    for i in range(tamaño):
                        tablero[fila+i, columna] = "O"
                    colocado = True
                else:
                    print("Orientación inválida. Usa H o V.")
            except:
                print("Entrada inválida. Intenta de nuevo.")
    return (tablero)  
              
'''
# Colocar barcos del rival
def colocar_barcos_aleatorio(tablero):
    for barco, tamaño in vr.barcos.items():
        colocado = False
        while not colocado:
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            orientacion = random.choice(["H", "V"])
            if orientacion == "H":
                if columna + tamaño > 10:
                    continue
                if any(tablero[fila, columna+i] == "O" for i in range(tamaño)):
                    continue
                for i in range(tamaño):
                    tablero[fila, columna+i] = "O"
                colocado = True
            else:
                if fila + tamaño > 10:
                    continue
                if any(tablero[fila+i, columna] == "O" for i in range(tamaño)):
                    continue
                for i in range(tamaño):
                    tablero[fila+i, columna] = "O"
                colocado = True
    return (vr.tablero_rival_barcos)

# Lógica del disparo
lista_disparos = []
def disparo(tablero):
    fila = int(input("selecciona la fila"))
    columna = int(input("selecciona la columna"))
    
    if tablero[fila,columna] =="O":
        tablero[fila,columna] = "X"
        print("¡Impacto!")
    elif tablero[fila,columna] == "#" or tablero[fila, columna] == "X":
        print ("Posiccion ya seleccionada. Pierdes el turno.")
        disparo(tablero)
    else:
        tablero[fila,columna] = "#"
        print ("Agua")

    return tablero
 
# Verificar si quedan barcos en un tablero
def quedan_barcos(tablero):
    return "O" in tablero   

turno = 1
while True:
    if turno % 2 != 0:
        # Jugador  dispara al tablero del rival
        utils.disparo(tablero_rival_barcos)
        print("\nTablero del rival:")
        print(vr.tablero_rival_barcos)
        if not utils.quedan_barcos(tablero_rival_barcos):
            print("¡Jugador gana!")
            break
    else:
        # Rival dispara al tablero del Jugador 
        utils.disparo(tablero_jugador_barcos)
        print("\nTablero del Jugador:")
        print(tablero_jugador_barcos)
        if not utils.quedan_barcos(tablero_jugador_barcos):
            print("¡Rival gana!")
            break
    turno += 1
'''

