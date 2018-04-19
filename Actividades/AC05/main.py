# Aqui van tus imports, estos pueden servirte
from collections import namedtuple
from itertools import tee
from functools import reduce

# from operator import attrgetter
# from functools import reduce

# ---------- FUNCIONES DE CSV ----------


def cleaner(line):
    *info, legendary = line.rstrip("\n").lower().split(",")
    return info + [legendary.lower() == "true"]

def obtener_data(nombre_archivo, nombre_tupla):
    """
    Esta función se utiliza para obtener un generador que les entregue los
    pokemones o entrenadores.

    Para generar pokemones deben usar "obtener_data('pokemondb.csv', 'Pokemon')"
    Para generar entrenadores, "obtener_data('entrenadoresdb.csv', 'Entrenador')"

    :param nombre_archivo: Nombre de la base de datos que deseen utilizar
    :param nombre_tupla: Nombre de las namedtuple
    :return: Generador de namedtuples
    """
    with open(nombre_archivo, mode="r", encoding="UTF-8") as file:
        data = file.readline().rstrip("\n").split(",")
        entidad = namedtuple(nombre_tupla, data)
        for line in file:
            yield entidad(*cleaner(line))


# ---------- FUNCIONES ----------


def pokedex_regional(generacion, pokemones):
    """
    Retorna un generador con todos los pokemones de cierta generación que
    se encuentran en el iterable pokemones.

    :param gen: int del 1 al 7
    :param pokemones: iterable de pokemones
    :return: generador
    """
    return (i for i in pokemones if i.generacion == str(generacion))
    


def obtener_estadistica(estadistica, pokemon):
    """
    Recibe una estadistica como string y un pokemon, y debe retornar el valor
    de la estadistica del pokemon.

    :param estadistica: string de estadistica
    :param pokemon: pokemon
    :return: int
    """

    return int(getattr(pokemon, estadistica))


def obtener_estadistica_promedio(estadistica, pokemones):
    """
    Recibe una estadistica en forma de string y un iterable de pokemones,
    y debe retornar el promedio de esa estadistica para todos los pokemones.

    :param estadistica: string de estadistica
    :param pokemones: iterable de pokemones
    :return: float
    """
    mapeo = map(lambda x: x.vida, pokemones)
    print (', '.join(mapeo))


    ## no funca :(
    pass


def pokemones_buena_estadistica(estadistica, pokemones):
    """
    Recibe una estadistica y un iterable de pokemones y
    debe retornar un generador de todos los pokemones
    cuya estadistica sea mejor que el promedio.

    :param estadistica: string de estadistica
    :param pokemones: iterable de pokemones
    :return: generador
    """
    pass


def pokemon_para_entrenador(entrenador, pokemones):
    """
    Recibe un entrenador y un iterable de pokemones y debe
    retornar un generador para los 6 mejores pokemones del entrenador.

    :param entrenador: entrenador
    :param pokemones: iterable de pokemones
    :return: generador
    """
    pass


def poder_total_entrenador(entrenador, pokemones):
    """
    Recibe un entrenador y un iterable de pokemones, 
    y retorna el poder total de este.

    :param entrenador: entrenador
    :param pokemones: iterable de pokemones
    :return: int
    """
    pass


# ---------- AQUI SE CORRE EL CÓDIGO ----------

#if __name__ == "__main__":
    # ------------- CONSULTA -------------
    # Aqui debe realizar la consulta de todos los Pokemon que se repitan en los equipos de cada entrenador con el
    # tipo favorito y estadistica favorita que se les entregó

    # -------------
    # TESTEOS
    # -------------
    # Hoja y ataque
    # -------------
    # Tsareena
    # Breloom
    # Dhelmise
    # Cacturne
    # -----------------------
    # Agua y defensa_especial
    # -----------------------
    # Mantine
    # Araquanid
    # Toxapex
    # Pyukumuku
    # -----------------------
    # Fuego y ataque_especial
    # -----------------------
    # Chandelure
    # Volcarona
#    pass

pokemones=obtener_data('pokemondb.csv', 'Pokemon')
#for i in pokedex_regional(1, pokemones):
#    print(obtener_estadistica("vida",i))
#    print(i)

    
print(obtener_estadistica_promedio("vida", pokemones))