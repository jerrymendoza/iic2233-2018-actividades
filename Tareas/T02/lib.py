from estructuras import ListaNoLinealJ
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
