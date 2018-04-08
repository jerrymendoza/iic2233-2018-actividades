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
        s+="Minerales: {} Deuterio: {}\n".format(self.minerales,self.deuterio)
        if len(self.planetas)>0:
            for i in self.planetas:
                s+="-{} \n".format(i.nombre.upper())
                s+="    -{}\n".format(i)
        else:
            s+="Esta Galaxia no tiene planetas \n"
        s+="\n"
        return s


    def construir_cuartel(self,planeta_index): 
        if not self.planetas[planeta_index].cuartel:
            if int(self.minerales) >= 200 and int(self.deuterio) >= 500:
                self.minerales -= 200
                self.deuterio -= 500
                self.planetas[planeta_index].cuartel = True
                print("Se ha construido un cuartel en {}".format(self.planetas[planeta_index].nombre))
            else:
                print("Recursos insuficientes!")
        else:
            print("Ya tienes un Cuartel!")

    def construir_torre(self,planeta_index):
        if not self.planetas[planeta_index].cuartel:
            if int(self.minerales) >= 150 and int(self.deuterio) >= 300:
                self.minerales -= 150
                self.deuterio -= 300
                self.planetas[planeta_index].torre = True
                print("Se ha construido un Cuartel en {}".format(self.planetas[planeta_index].nombre.upper()))
            else:
                print("Recursos insuficientes!")
        else:
            print("Ya tienes una Torre de defensa!")

    def generar_unidades(self,planeta_index,cantidad=1,tipo="soldado"):
        if self.planetas[planeta_index].cuartel:
            if tipo=="soldado":
                if self.planetas[planeta_index].costo_soldado[0]*cantidad <= self.minerales and self.planetas[planeta_index].costo_soldado[1]*cantidad <= self.deuterio:
                    self.planetas[planeta_index].soldados += cantidad
                else:
                    print("Recursos insuficientes")

            elif tipo=="mago" and self.planetas[planeta_index].raza == "maestro":
                if self.planetas[planeta_index].costo_mago[0]*cantidad <= self.minerales and self.planetas[planeta_index].costo_mago[1]*cantidad <= self.deuterio:
                    self.planetas[planeta_index].magos += cantidad
                else:
                    print("Recursos insuficientes")
        else:
            print("Primero necesitas un Cuartel")

    def recolectar_recursos(self):
        #mejorar nivel de ataque o nivel de economia
        pass

    def invadir_planeta(self):
        pass

    def comprar_planeta(self):
        #1.000.000 minerales y 500.000 deuterio
        pass

class Planeta:
    """docstring for Planeta"""
    def __init__(self, nombre,**kwargs):
        self.nombre = nombre.lower()
        self.tasa_minerales = kwargs.get('tasa_minerales',
                                         random.randint(1, 10)) 
        self.tasa_deuterio = kwargs.get('tasa_deuterio',
                                         random.randint(5, 15))
        self.ultima_recoleccion=kwargs.get('ultima_recoleccion',
                                         datetime.now())
        self.__nivel_ataque = kwargs.get('nivel_ataque',0) 
        self.__nivel_economia = kwargs.get('nivel_economia',0)
        self.conquistado = kwargs.get('conquistado',False)
        self.cuartel = kwargs.get('cuartel',False)
        self.torre = kwargs.get('torre',False)

        #####
        self.raza = ""
        self.poblacion_max = 0
        self.costo_soldado = 0
        self.costo_mago = 0
        self.__soldados = kwargs.get('soldados',0) 
        self.__magos = kwargs.get('magos',0) 
        self.ataque_soldado = 0
        self.__ataque_mago = 0
        self.__vida_soldado = 0
        self.__vida_mago = 0

    def __repr__(self):
        s = [self.raza, 
             str(self.soldados),
             str(self.magos),
             str(self.ultima_recoleccion.strftime("%Y-%m-%d %H:%M:%S")),
             str(self.nivel_ataque),
             str(self.nivel_economia),
             str(self.conquistado),
             str(self.cuartel),
             str(self.torre),
             str(self.evolucion())]
        s = ','.join(s)
        return s

    @property
    def edificios(self):
        return self.__edificios


    @property
    def nivel_ataque(self):
        return self.__nivel_ataque

    @nivel_ataque.setter
    def nivel_ataque(self,p):
        if p <= 3:
            self.__nivel_ataque += p

    @property
    def nivel_economia(self):
        return self.__nivel_economia

    @nivel_economia.setter
    def nivel_economia(self,p):
        if p <= 3:
            self.__nivel_economia += p

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

    def evolucion(self):
        total=self.nivel_economia+self.nivel_ataque
        total+=((self.magos+self.soldados)/self.poblacion_max)+self.cuartel
        total+=self.torre
        return round(total, 1)

class Maestro(Planeta):
    """docstring for Maestro"""
    def __init__(self, nombre,**kwargs):
        super().__init__(nombre,**kwargs)
        self.raza = "maestro"
        self.poblacion_max = 100
        self.costo_soldado = (200,300)
        self.costo_mago = (300,400)
        self.__ataque_soldado = random.randint(60, 80)
        self.__ataque_mago = random.randint(80, 120)
        self.__vida_soldado = random.randint(200, 250)
        self.__vida_mago = random.randint(150, 200)
        self.grito = "¡Nuestro conocimiento nos ha otorgado uan victoria más!"



class Aprendiz(Planeta):
    """docstring for Aprendiz"""
    def __init__(self, nombre,**kwargs):
        super().__init__(nombre, **kwargs)
        self.raza = "aprendiz"
        self.poblacion_max = 150
        self.__soldados = kwargs.get('soldados',0) 
        self.costo_soldado = (300,400)
        self.ataque_soldado = random.randint(30, 60)
        self.__vida_soldado = random.randint(600, 700)
        self.grito = "¡Con una gran defensa y medicinas, nuestros soldados " \
                     "son invencibles!"        



class Asesino(Planeta):
    """docstring for Asesino"""
    def __init__(self, nombre, **kwargs):
        super().__init__(nombre, **kwargs)
        self.raza = "asesino"
        self.poblacion_max = 400
        self.__soldados = kwargs.get('soldados',0) 
        self.costo_soldado = (100,200)
        self.ataque_soldado = random.randint(40, 45)
        self.__vida_soldado = random.randint(250, 270)
        self.grito = "¡El poder de las sombras es lo unico necesario para " \
                     "ganar estas batallas!"

