
from lib import read_csv,poblar,elegir_galaxia,elegir_planeta,elegir_planeta_noconquistado 
from misclases import Galaxia,Maestro,Aprendiz,Asesino



galaxias=[]
actual=[None,None]
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
    print('\n') 
    if seleccion =='1': 
        print("- Cargar CSV -".center(80))
        poblar(galaxias)

    elif seleccion == '2': 
        print("- Crear Galaxia -".center(80))
        nombre_galaxia=input("Nombre para la Galaxia nueva: ")
        galaxias.append(Galaxia(nombre_galaxia))

        while True:
            menu2 = {}
            menu2['1']="Agregar Planeta a Galaxia {}".format(galaxias[-1].nombre) 
            menu2['2']="Terminar"
            opciones2=list(menu2.keys())
            opciones2.sort()
            for entry in opciones2:
                print("     ({}) {}".format(entry, menu2[entry]))
            seleccion2=input("Seleccion:")
            print('\n')  
            if seleccion2 =='1':
                print("- {} -".format(menu2['1']).center(80))
                n=input("Nombre del nuevo planeta:")
                print("\n")
                print("Elegir Raza para {}".format(n).upper())
                while True:
                    menu2a = {}
                    menu2a['1']="Maestro" 
                    menu2a['2']="Aprendiz"
                    menu2a['3']="Asesino"
                    opciones2a=list(menu2a.keys())
                    opciones2a.sort()
                    for entry in opciones2a:
                        print("     ({}) {}".format(entry, menu2a[entry]))
                    seleccion2a=input("Seleccion:")
                    print('\n')
                    if seleccion2a =='1':
                        galaxias[-1].planetas.append(Maestro(n))
                        break
                    elif seleccion2a == '2':
                        galaxias[-1].planetas.append(Aprendiz(n))
                        break
                    elif seleccion2a == '3':
                        galaxias[-1].planetas.append(Asesino(n))
                        break 
                    else:
                        print("No valido!")

            elif seleccion2 == '2':
                print("Elegir Planeta incial para Galaxia {}".format(galaxias[-1].nombre))
                aux=0
                for planeta in galaxias[-1].planetas:
                    aux+=1
                    print("({}) {} de la Raza {}".format(aux,planeta.nombre.upper(),planeta.raza.upper()) )

                select=int(input("Seleccion: "))
                select-=1

                for i in range(len(galaxias[-1].planetas)):
                    if select!=i:
                        galaxias[-1].planetas[i].poblar75()
                    else:
                        galaxias[-1].planetas[select].conquistado=True
                print(galaxias[-1])
                print("Estas Listo para Jugar!")

                break
            else:
                print("No valido!")
        
        #crear galaxia y planetas
        #UN planeta debe quedar connquistado del principio

    elif seleccion == '3':
        print("- Modificar Galaxia -".center(80))
        actual=elegir_galaxia(galaxias,actual)


        # usar actual[0]
        menu3 = {}
        menu3['1']="Agregar Planeta (sin conquistar)" 
        menu3['2']="Eliminar Planeta ya conquistado"
        menu3['3']="Aumentar tasa minerales (sin conquistar)"
        menu3['4']="Aumentar tasa deuterio (sin conquistar)"
        menu3['5']="Aumentar soldados (sin conquistar)"
        menu3['6']="Aumentar magos (sin conquistar)"
        menu3['7']="Volver"

        while True:
            opciones3=list(menu3.keys())
            opciones3.sort()
            for entry in opciones3:
                print("     ({}) {}".format(entry, menu3[entry]))
            seleccion3=input("Seleccion:")
            print('\n')  
            if seleccion3 =='1':
                print("- {} -".format(menu3['1']).center(80))
                n=input("Nombre del nuevo planeta:")
                print("\n")
                print("Elegir Raza para {}".format(n).upper())
                while True:
                    menu3a = {}
                    menu3a['1']="Maestro" 
                    menu3a['2']="Aprendiz"
                    menu3a['3']="Asesino"
                    opciones3a=list(menu3a.keys())
                    opciones3a.sort()
                    for entry in opciones3a:
                        print("     ({}) {}".format(entry, menu3a[entry]))
                    seleccion3a=input("Seleccion:")
                    print('\n')
                    if seleccion3a =='1':
                        galaxias[actual[0]].planetas.append(Maestro(n))
                        break
                    elif seleccion3a == '2':
                        galaxias[actual[0]].planetas.append(Aprendiz(n))
                        break
                    elif seleccion3a == '3':
                        galaxias[actual[0]].planetas.append(Asesino(n))
                        break 
                    else:
                        print("No valido!")

                print("Planeta Creado")
            elif seleccion3 == '2':
                print("- {} -".format(menu3['2']).center(80))
                #eliminar planeta

            elif seleccion3 == '3':
                print("- {} -".format(menu3['3']).center(80))
                actual=elegir_planeta_noconquistado(galaxias,actual)
                n=int(input("Cuanto desea aumentar la tasa de minerales: "))
                galaxias[actual[0]].planetas[actual[1]].aumentar(n,"mineral")
                print("Listo!")
                break
                
            elif seleccion3 == '4':
                print("- {} -".format(menu3['4']).center(80))
                actual=elegir_planeta_noconquistado(galaxias,actual)
                n=int(input("Cuanto desea aumentar la tasa de deuterio: "))
                galaxias[actual[0]].planetas[actual[1]].aumentar(n,"deuterio")
                print("Listo!")
                break
            elif seleccion3 == '5':
                print("- {} -".format(menu3['5']).center(80))
                actual=elegir_planeta_noconquistado(galaxias,actual)
                n=int(input("Cuandos soldados desea agregar: "))
                galaxias[actual[0]].planetas[actual[1]].aumentar(n,"soldado")
                print("Listo!")
                break
            elif seleccion3 == '6':
                print("- {} -".format(menu3['6']).center(80))
                actual=elegir_planeta_noconquistado(galaxias,actual)
                n=int(input("Cuandos magos desea agregar: "))
                galaxias[actual[0]].planetas[actual[1]].aumentar(n,"magos")
                print("Listo!")
                break
            elif seleccion3 == '7': 
                break
            else: 
                print("No valido!")

    elif seleccion == '4':
        print("- Consultar Galaxias -".center(80))
        
        menu4 = {}
        menu4['1']="Informacion General Usuario"
        menu4['2']="Informacion General Planeta"
        menu4['3']="Mejor Galaxia"
        menu4['4']="Ranking de Planetas"
        menu4['5']="Volver"

        while True:
            opciones4=list(menu4.keys())
            opciones4.sort()
            for entry in opciones4:
                print("     ({}) {}".format(entry, menu4[entry]))
            seleccion4=input("Seleccion:")
            print('\n')  
            if seleccion4 =='1':
                print("- {} -".format(menu4['1']).center(80))
                for galaxia in galaxias:
                    galaxia.mostrar_conquistados()

            elif seleccion4 == '2':

                actual=elegir_galaxia(galaxias,actual)
                actual=elegir_planeta(galaxias,actual) 
                print("- {} -".format(menu4['2']).center(80))
                print("Informacion de Planeta {} de la Galaxia {}:".format(
                    galaxias[actual[0]].planetas[actual[1]].nombre,
                    galaxias[actual[0]].nombre))
                galaxias[actual[0]].planetas[actual[1]].info_general()

            elif seleccion4 == '3':
                print("3")

            elif seleccion4 == '4':
                actual=elegir_galaxia(galaxias,actual)
                # usar actual[0]
                print("4")

            elif seleccion4 == '5': 
                break

            else: 
                print("No valido!")

        else:
            print("No hay galaxias aun!")

       

    elif seleccion == '5':
        print("- Jugar -".center(80))
        #primero elegir galaxia y planeta

        actual=elegir_galaxia(galaxias,actual)
        # usar actual[0]
        actual=elegir_planeta(galaxias,actual)

        menu5 = {}
        menu5['1']="Construir Edificio" 
        menu5['2']="Generar Unidades"
        menu5['3']="Recolectar Recursos"
        menu5['4']="Realizar Mejoras"
        menu5['5']="Volver"

        while True:
            opciones5=list(menu5.keys())
            opciones5.sort()
            for entry in opciones5:
                print("     ({}) {}".format(entry, menu5[entry]))
            seleccion5=input("Seleccion:")
            print('\n')  
            if seleccion5 =='1':
                print("- {} -".format(menu5['1']).center(80))
                print(" (1) ")
            elif seleccion5 == '2':
                print("2")
            elif seleccion5 == '3':
                print("3")
            elif seleccion5 == '4':
                print("4")
            elif seleccion5 == '5': 
                break
            else: 
                print("No valido!") 
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


