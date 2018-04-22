from estructuras import ListaNoLinealJ,ArbolAVL,ListaJ
from misclases import Jugador

def leer(path):
    dic = ListaNoLinealJ()  #diccionario en un arbolAVL
    with open(path,'r', encoding="UTF-8") as file:
        aux=False
        for linea in file:
            if aux:
                a=Jugador(*linea.strip().split(','))
                dic[a.id]=a
            aux=True
    return dic


def crear_grafo(jugadores):
    #retorna grafo con los jugadores
    nacionalidad=ArbolAVL()
    club=ArbolAVL()
    liga=ArbolAVL()

    for jugador in jugadores:
        if jugador.nationality not in nacionalidad:
            nacionalidad[jugador.nationality]=ListaJ()
        if jugador.club not in club:
            club[jugador.club]=ListaJ()
        if jugador.league not in liga:
            liga[jugador.league]=ListaJ()

        nacionalidad[jugador.nationality].append(jugador.id)
        club[jugador.club].append(jugador.id)
        liga[jugador.league].append(jugador.id)


    #print("por nacionalidad:")
    print(nacionalidad)
    #print("por club:")
    #print(club)
    #print("por liga:")
    #print(liga)
    #print(nacionalidad["Chile"].existe_valor(184941))
    for jugador in jugadores:
        print("sadkfhñadkfshajfsdk")
        print(jugador)
        print(nacionalidad[jugador.nationality])
        print("sadkfhñadkfshajfsdk")
        for id_jugador in nacionalidad[jugador.nationality]:

            if not id_jugador==jugador.id:
                print("------------")
                print(jugador.id)
                print(jugador.club)
                print(club[jugador.club])
                print(id_jugador)
                print("------------")
                if club[jugador.club].existe_valor(id_jugador):
                    #print("Amigos cercanos!! {} - {}".format(jugador.id,id_jugador))
                    #print(jugadores[jugador.id])
                    #print(jugadores[id_jugador])
                    print("a")

                elif liga[jugador.league].existe_valor(id_jugador):
                    #print("Amigos lejanos!! {} - {}".format(jugador.id,id_jugador))
                    #print(jugadores[jugador.id])
                    #print(jugadores[id_jugador])
                    print("b")
                else: 
                    #print("parece que son conocidos {} - {}".format(jugador.id,id_jugador))
                    #print(jugadores[jugador.id])
                    #print(jugadores[id_jugador])
                     print("c")




if __name__ == "__main__":
    jugadores=leer("players_db_chica.csv")
    crear_grafo(jugadores)

