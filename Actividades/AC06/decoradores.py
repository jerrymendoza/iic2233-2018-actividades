"""
-- decoradores.py --

Escriba, en este archivo, todos sus decoradores.
"""

FILENAME = 'registro.txt'

def registrar(funcion):
    def decorar(*args):
        retorno = funcion(*args)
        file = open(FILENAME, "a")
        file.write("{} {} \n".format(funcion.__name__,args, retorno))
        file.close()
        return retorno
    return decorar


def verificar_tipos(*tipos):
    def _verificar_tipos(funcion):
        def decorada(*args):
            if not len(tipos) == len(args):
                raise TypeError("La cantidad de argumentos de la funcion no coincide con la cantidad de argumentos entregados")
            for i in range(len(args)):
                if not isinstance(args[i],tipos[i]):
                    raise TypeError("El {} no es del tipo {}".format(args[i],tipos[i]))



