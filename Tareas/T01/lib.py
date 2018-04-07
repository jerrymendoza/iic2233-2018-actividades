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

        aux = list(zip(*aux2))
    elif tipe=="galaxia":
        aux = list(zip(*aux.values()))

    return aux