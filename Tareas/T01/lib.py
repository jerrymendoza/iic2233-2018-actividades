from misclases import Galaxia,Maestro,Aprendiz,Asesino
from datetime import datetime

def read_csv(path,tipe):
    aux = []
    aux2 = []
    planetas_titulos = ['nombre: string', 'galaxia: string', 'raza: string',
                 'magos: int', 'soldados: int', 'tasa_minerales: int',
                 'tasa_deuterio: int', 'ultima_recoleccion: datetime',
                 'nivel_ataque: int', 'nivel_economia: int',
                 'conquistado: bool', 'torre: bool', 'cuartel: bool']
    with open(path,'r', encoding="UTF-8") as file:
        for linea in file:
            aux.append(linea.strip().split(', '))

    aux = dict(zip(aux[0],list(zip(*aux[1:]))))
    if tipe=="planeta":
        for titulo in planetas_titulos:
            aux2.append(aux[titulo])

        return list(zip(*aux2))
    elif tipe=="galaxia":
        return list(zip(*aux.values()))


def poblar(galaxias):   
    for i in read_csv('galaxias.csv','galaxia'):
        galaxias.append(Galaxia(i[0],minerales=int(i[1]),deuterio=int(i[2])))
    
    for planeta in read_csv('planetas.csv','planeta'):
        for galaxia in galaxias:
            if galaxia.nombre == planeta[1].lower():
                if planeta[2].lower() == "maestro":
                    galaxia.planetas.append(Maestro(
                                   planeta[0],
                                   magos=int(planeta[3]),
                                   soldados=int(planeta[4]),
                                   tasa_minerales=int(planeta[5]),
                                   tasa_deuterio=int(planeta[6]),
                                   ultima_recoleccion=
                                                datetime.strptime(planeta[7],
                                                "%Y-%m-%d %H:%M:%S"),
                                   nivel_ataque=int(planeta[8]),
                                   nivel_economia=int(planeta[9]),
                                   conquistado=planeta[10]=="True",
                                   torre=planeta[11]=="True",
                                   cuartel=planeta[12]=="True"
                                   ))
                elif planeta[2].lower() == "aprendiz":
                    galaxia.planetas.append(Aprendiz(
                                   planeta[0],
                                   soldados=int(planeta[4]),
                                   tasa_minerales=int(planeta[5]),
                                   tasa_deuterio=int(planeta[6]),
                                   ultima_recoleccion=
                                                datetime.strptime(planeta[7],
                                                "%Y-%m-%d %H:%M:%S"),
                                   nivel_ataque=int(planeta[8]),
                                   nivel_economia=int(planeta[9]),
                                   conquistado=planeta[10]=="True",
                                   torre=planeta[11]=="True",
                                   cuartel=planeta[12]=="True"
                                   ))
                elif planeta[2].lower() == "asesino":
                    galaxia.planetas.append(Asesino(
                                   planeta[0],
                                   soldados=int(planeta[4]),
                                   tasa_minerales=int(planeta[5]),
                                   tasa_deuterio=int(planeta[6]),
                                   ultima_recoleccion=
                                                datetime.strptime(planeta[7],
                                                "%Y-%m-%d %H:%M:%S"),
                                   nivel_ataque=int(planeta[8]),
                                   nivel_economia=int(planeta[9]),
                                   conquistado=planeta[10]=="True",
                                   torre=planeta[11]=="True",
                                   cuartel=planeta[12]=="True"
                                   ))



def elegir_galaxia(galaxias,actual):
    if len(galaxias)>0:
        for i in range(len(galaxias)):
            print("     ({}) {}".format(i+1,galaxias[i].nombre))
        actual[0]=int(input("Elegir Galaxia:"))  
    else: 
        print("No hay Galaxias creadas")
    return actual

def elegir_planeta(galaxias,actual):
    if len(galaxias[actual[0]].planetas)>0:
        for i in range(len(galaxias[actual[0]].planetas)):
            print("     ({}) {}".format(i+1,galaxias[actual[0]].planetas[i].nombre))
        actual[1]=int(input("Elegir Planeta:"))
    else:
        print("No hay Planetas aca!")
    return actual

