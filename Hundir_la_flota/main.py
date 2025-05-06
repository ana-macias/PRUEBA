import utils

barco_1 = [[0,3],[0,4],[0,5],[0,6]]

tablero = utils.crear_tablero()
print (tablero)
print ("______________________")
tablero_modificado = utils.colocar_barco (tablero,barco_1)

print (tablero_modificado)