from estructuras import ListaJ,ArbolAVL,ListaNoLinealJ
from misclases import Jugador
from lib import leer



dic=leer("players_db_chica.csv")



for i in dic:
    print(i)

for i in dic:
    print(i.id)



print("total:"+str(len(dic)))
