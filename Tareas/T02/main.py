from estructuras import ListaJ
from misclases import Jugador
def poblar(path):
    lista = ListaJ()
    with open(path,'r', encoding="UTF-8") as file:
        aux=False
        for linea in file:
            if aux:
               lista.append(Jugador(*linea.strip().split(',')))
            aux=True
    return lista


lista=poblar("players_db_chica.csv")
for i in lista:
    print(i)