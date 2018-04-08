
from lib import read_csv,poblar 
from misclases import Galaxia,Maestro,Aprendiz,Asesino



galaxias=[]
#print(read_csv('planetas.csv','planeta'))



print("{} ChauCraft {}".format("*"*20,"*"*20).center(80))

menu = {}
menu['1']="Cargar Archivos csv" 
menu['2']="Crear Galaxia"
menu['3']="Modificar una Galaxia"
menu['4']="Consultar sobre una Galaxia"
menu['5']="Jugar en una Galaxia"
menu['6']="Exit"
while True: 
    opciones=list(menu.keys())
    opciones.sort()
    for entry in opciones: 
        print("     ({}) {}".format(entry, menu[entry]))

    seleccion=input("Seleccion:") 
    if seleccion =='1': 
        print("cargar csv")
        poblar(galaxias)

    elif seleccion == '2': 
        print("crear galaxia")
        nombre_galaxia=input("Nombre para la Galaxia nueva: ")
        galaxias.append(Galaxia(nombre_galaxia))

    elif seleccion == '3':
        print("modificar galaxia")

    elif seleccion == '4':
        print("Consultar galaxias")
        if len(galaxias):
            print(*galaxias)
        else:
            print("No hay galaxias aun!")

    elif seleccion == '5':
        print("Jugar")
        #visitar un planeta
            #(conquistado)
            #construir edificio
            #generar unidades
            #recolectar recursos
            #realizar mejoras
            
            #(no conquistado)
            #invadir planeta
            #comprar el planeta

        

    elif seleccion == '6': 
        break

    else: 
        print("No valido!")


