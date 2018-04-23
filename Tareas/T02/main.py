from estructuras import ListaJ,ArbolAVL,ListaNoLinealJ
from misclases import Jugador
from lib import leer,crear_grafo



jugadores=leer("players_db_chica.csv")




print("total:"+str(len(jugadores)))


graf=crear_grafo(jugadores)
graf.imp()
print("Jugador mas popular: ")

print(jugadores[graf.mas_popular()])
