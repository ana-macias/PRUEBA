import utils_copy
import variables_copy as vr

tablero_rival_barcos = utils_copy.crear_tablero ()  # Muestra el barco del rival y los disparos del jugador
tablero_rival_disparos = utils_copy.crear_tablero () # Muestra los disparos del rival

tablero_jugador_barcos = utils_copy.crear_tablero () # Muestra tus barcos y los disparos rival
tablero_jugador_disparos = utils_copy.crear_tablero () # Muestra los disparos del jugadores



print("TABLERO DONDE SE MUESTRAN LOS BARCOS DEL RIVAL Y LOS DISPAROS DEL JUGADOR.")
print(vr.tablero_rival_barcos)

print("TABLERO DONDE SE MUESTRA LOS BARCOS DEL JUGADOR Y LOS DISPAROS DEL RIVAL")
print(vr.tablero_jugador_barcos)





