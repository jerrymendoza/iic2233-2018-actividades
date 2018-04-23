from estructuras import ListaNoLinealJ,ArbolAVL,ListaJ,Grafo
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
    #print(nacionalidad)
    #print("por club:")
    #print(club)
    #print("por liga:")
    #print(liga)
    #print(nacionalidad["Chile"].existe_valor(184941))
    graf=Grafo()
    for jugador in jugadores:
        for id_jugador in nacionalidad[jugador.nationality]:
            if not id_jugador==jugador.id:
                
                if club[jugador.club].existe_valor(id_jugador):
                    graf.agregar_arista(jugador.id,id_jugador,1)
                elif liga[jugador.league].existe_valor(id_jugador):
                    graf.agregar_arista(jugador.id,id_jugador,0.95)
                else: 
                    graf.agregar_arista(jugador.id,id_jugador,0.9)
        for id_jugador in club[jugador.club]:
            if not id_jugador==jugador.id:
                if (not nacionalidad[jugador.nationality].existe_valor(id_jugador) and 
                    not liga[jugador.league].existe_valor(id_jugador)):
                         graf.agregar_arista(jugador.id,id_jugador,0.9)
        for id_jugador in liga[jugador.league]:
            if not id_jugador==jugador.id:
                if (not nacionalidad[jugador.nationality].existe_valor(id_jugador) and 
                    not club[jugador.club].existe_valor(id_jugador)):
                         graf.agregar_arista(jugador.id,id_jugador,0.9)

    return graf

if __name__ == "__main__":
    jugadores=leer("players_db_chica.csv")
    graf=crear_grafo(jugadores)
    graf.imp()
