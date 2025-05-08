import utils
import variables as vr

tablero_rival_barcos = utils.crear_tablero ()  # Muestra el barco del rival y los disparos del jugador
tablero_rival_disparos = utils.crear_tablero () # Muestra los disparos del rival

tablero_jugador_barcos = utils.crear_tablero () # Muestra tus barcos y los disparos rival
tablero_jugador_disparos = utils.crear_tablero () # Muestra los disparos del jugador


tablero_rival_barcos = utils.colocar_barcos (tablero_rival_barcos, vr.barco_jugador)
print (tablero_rival_barcos)

tablero_rival_disparos = utils.disparo

print ("_________________________")

tablero_rival_barcos = utils.crear_tablero ()
tablero_rival_barcos = utils.colocar_barcos (tablero_rival_barcos, vr.barco_rival)
print ("TABLERO JUGADOR")
print (tablero_rival_barcos)

tablero_jugador_disparos = utils.disparo (tablero_jugador_disparos)
print (tablero_jugador_disparos)
