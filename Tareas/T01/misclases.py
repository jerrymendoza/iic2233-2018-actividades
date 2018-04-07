import random
from datetime import datetime
class Galaxia:
    """docstring for Galaxia"""
    def __init__(self, nombre,**kwargs):
        self.nombre = nombre.lower()
        self.planetas = []
        self.minerales = kwargs.get('minerales',0)
        self.deuterio = kwargs.get('deuterio',0)
    def __repr__(self):
        s = "***** {} *****\n".format(self.nombre.upper())
        if len(self.planetas)>0:
            for i in self.planetas:
                s+="- {} \n".format(i.nombre.capitalize())
        else:
            s+="Esta Galaxia no tiene planetas"
        return s


class Planeta:
    """docstring for Planeta"""
    def __init__(self, nombre,**kwargs):
        self.nombre = nombre.lower()
        self.tasa_minerales = kwargs.get('tasa_minerales') #tasa minerales x segundo
        self.tasa_deuterio = kwargs.get('tasa_deuterio',0)
        self.cuartel = kwargs.get('cuartel',False)
        self.torre = kwargs.get('torre',False)
        self.ultima_recoleccion = kwargs.get('ultima_recoleccion',datetime.now())
        self.__nivel_ataque = kwargs.get('nivel_ataque',0) 
        self.__nivel_economia = kwargs.get('nivel_economia',0)
        self.conquistado = kwargs.get('conquistado',False)
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
    def __init__(self, nombre,**kwargs):
        super().__init__(nombre,**kwargs)
        self.raza = "maestro"
        self.poblacion_max = 100
        self.__soldados = kwargs.get('soldados',0) 
        self.__magos = kwargs.get('magos',0) 
        self.__costo_soldado = (200,300)
        self.__costo_mago = (300,400)
        self.__ataque_soldado = random.randint(60, 80)
        self.__ataque_mago = random.randint(80, 120)
        self.__vida_soldado = random.randint(200, 250)
        self.__vida_mago = random.randint(150, 200)
        self.grito = "¡Nuestro conocimiento nos ha otorgado uan victoria más!"

    def __repr__(self):
        s = "{}".format(self.raza) 

    @property
    def soldados(self):
        return self.__soldados

    @soldados.setter
    def soldados(self, p):
        if p + self.magos <= self.poblacion_max:
            self.__soldados += p

    @property
    def magos(self):
        return self.__magos

    @magos.setter
    def magos(self,p):
        if self.soldados + p <= self.poblacion_max:
            self.__magos += p

class Aprendiz(Planeta):
    """docstring for Aprendiz"""
    def __init__(self, nombre,**kwargs):
        super().__init__(nombre, **kwargs)
        self.raza = "aprendiz"
        self.poblacion_max = 150
        self.__soldados = kwargs.get('soldados',0) 
        self.__costo_soldado = (300,400)
        self.__ataque_soldado = random.randint(30, 60)
        self.__vida_soldado = random.randint(600, 700)
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
    def __init__(self, nombre, **kwargs):
        super().__init__(nombre, **kwargs)
        self.raza = "asesino"
        self.poblacion_max = 400
        self.__soldados = kwargs.get('soldados',0) 
        self.__costo_soldado = (100,200)
        self.__ataque_soldado = random.randint(40, 45)
        self.__vida_soldado = random.randint(250, 270)
        self.grito = "¡El poder de las sombras es lo unico necesario para " \
                     "ganar estas batallas!"

    @property
    def soldados(self):
        return self.__soldados

    @soldados.setter
    def soldados(self, p):
        if p + self.magos <= self.poblacion_max:
            self.__soldados = p