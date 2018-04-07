class Galaxia:
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


class Planeta:
    """docstring for Planeta"""
    def __init__(self, nombre):
        self.nombre = nombre.lower()
        self.tasa_minerales = 0 #tasa minerales x segundo
        self.tasa_deuterio = 0 #tasa deuterio x segundo
        self.cuartel = False
        self.torre = False
        self.ultima_recoleccion = 56676 #ultima recoleccion
        self.__nivel_ataque = 0
        self.__nivel_economia = 0
        self.conquistado = False
        self.__evolucion = 0


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
    def nivel_economia(self):
        return self.__nivel_econo

    @nivel_economia.setter
    def evolucion(self,p):
        if p <= 3:
            self.__nivel_economia = p


class Maestro(Planeta):
    """docstring for Maestro"""
    def __init__(self, nombre):
        super().__init__(nombre)
        self.raza = "maestro"
        self.poblacion_max = 100
        self.__soldados = 0 
        self.__magos = 0
        self.__costo_soldado = 0
        self.__costo_mago = 0
        self.__ataque_soldado = 0
        self.__ataque_mago = 0
        self.__vida_soldado = 0
        self.__vida_mago = 0
        self.grito = "¡Nuestro conocimiento nos ha otorgado uan victoria más!"

    def __repr__(self):
        s = "{}".format(self.raza) 

    @property
    def soldados(self):
        return self.__soldados

    @soldados.setter
    def soldados(self, p):
        if p + self.magos <= self.poblacion_max:
            self.__soldados = p

    @property
    def magos(self):
        return self.__magos

    @magos.setter
    def magos(self,p):
        if self.soldados + p <= self.poblacion_max:
            self.__magos = p

class Aprendiz(Planeta):
    """docstring for Aprendiz"""
    def __init__(self, nombre):
        super().__init__(nombre)
        self.raza = "aprendiz"
        self.poblacion_max = 150
        self.__soldados = 0 
        self.__costo_soldado = 0
        self.__ataque_soldado = 0
        self.__vida_soldado = 0
        self.grito = "¡Con una gran defensa y medicinas, nuestros soldados " \
                     "son invencibles!"        


    @property
    def soldados(self):
        return self.__soldados

    @soldados.setter
    def soldados(self, p):
        if p + self.magos <= self.poblacion_max:
            self.__soldados = p

class Asesino(Planeta):
    """docstring for Asesino"""
    def __init__(self, nombre):
        super().__init__(nombre)
        self.raza = "asesino"
        self.poblacion_max = 400
        self.__soldados = 0 
        self.__costo_soldado = 0
        self.__ataque_soldado = 0
        self.__vida_soldado = 0
        self.grito = "¡El poder de las sombras es lo unico necesario para " \
                     "ganar estas batallas!"

    @property
    def soldados(self):
        return self.__soldados

    @soldados.setter
    def soldados(self, p):
        if p + self.magos <= self.poblacion_max:
            self.__soldados = p