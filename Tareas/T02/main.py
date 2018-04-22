from estructuras import ListaJ,ArbolAVL,ListaNoLinealJ
from misclases import Jugador
def poblar(path):
    dic = ListaNoLinealJ()  #diccionario en un arbolAVL
    with open(path,'r', encoding="UTF-8") as file:
        aux=False
        for linea in file:
            if aux:
                a=Jugador(*linea.strip().split(','))
                dic[a.id]=a
            aux=True
    return dic


dic=poblar("players_db_chica.csv")



for i in dic:
    print(i)

print("total:"+str(len(dic)))

