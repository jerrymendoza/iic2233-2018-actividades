class Galaxia(object):
    """docstring for Galaxia"""
    def __init__(self, nombre):
        self.nombre = nombre.lower()
        self.planetas = []
    def __repr__(self):
        s = "***** {} *****\n".format(self.nombre.upper())
        if len(planetas)>0:
            for i in planetas:
                s+="- {} \n".format(i.nombre.capitalize())
        else:
            s+="Esta Galaxia no tiene planetas"
        return s

class Planeta(object):
    """docstring for Planeta"""
    def __init__(self, nombre, raza):
        self.nombre = nombre.lower()
        self.raza = raza
        self.__nsoldados = 0 #verificar con p_max
        self.__nmagos = 0 #verificar con p_max
        self.p_max = 0
        self.t_mxs = 0 #tasa minerales x segundo
        self.t_dxs = 0 #tasa deuterio x segundo
        self.__edificios = [0,0] #[cuartel,torre de defensa]
        self.recoleccion = 0 #ultima recoleccion
        self.__nivel_ataque = 0
        self.__nivel_econo = 0
        self.conquistado = False
        self.__evolucion = 0

    def __repr__(self):
        s="{},{}".format(self.nombre.capitalize(),self.raza)

    @property
    def nsoldados(self):
        return self.__nsoldados

    @nsoldados.setter
    def nsoldados(self, p):
        if self.nsoldados + self.nmagos <= self.p_max:
            self.__nsoldados = p

    @property
    def nmagos(self):
        return self.__nmagos

    @nmagos.setter
    def nmagos(selg,p):
        if self.nsoldados + self.nmagos <= self.p_max:
            self.__nmagos = p

    @property
    def edificios(self):
        return self.__edificios


    @property
    def nivel_ataque(self):
        return self.__nivel_ataque

    @nivel_ataque.setter
    def evolucion(self,p):
        if p <= 3:
            self.__nivel_ataque = p

    @property
    def nivel_econo(self):
        return self.__nivel_econo

    @nivel_econo.setter
    def evolucion(self,p):
        if p <= 3:
            self.__nivel_econo = p