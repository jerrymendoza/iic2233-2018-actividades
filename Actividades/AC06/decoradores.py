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
    def verificar_tipos2(funcion):
        def decorada(*args):
            if not len(tipos)+1 ==len(args):
                raise TypeError("La cantidad de argumentos de la funcion no coincide con la cantidad de argumentos entregados")
            for i in range(len(args)-1):
                if not isinstance(args[i+1],tipos[i]):
                    raise TypeError("El {} no es del tipo {}".format(args[i+1],tipos[i]))

        return decorada
    return verificar_tipos2

