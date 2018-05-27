from lib import read_csv
from faker import Faker
import params

class Persona():
    """ """
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido


class Empleado(Persona):
    """ """
    def __init_(self):
        pass

class Cliente(Persona):
    """ """
    def __init__(self):
        self._energia = 1
        self._hambre = random.randint(1, 25)/100
        #self.paciencia = 
        self.nauseas = 0
    @property
    def energia(self):
        return self._energia
    
    @energia.setter
    def energia(self, value):
        if value >=1:
            self._energia = 1
        elif value <= 0:
            self._energia = 0
        else:
            self._energia = value

    @property
    def hambre(self):
        return self._hambre
    
    @hambre.setter
    def hambre(self, value):
        if value >=1:
            self._hambre = 1
        elif value <= 0:
            self._hambre = 0
        else:
            self._hambre = value
    

class Adulto(Cliente):
    def __init__(self):
        #self.presupuesto =
        #self.niños 
        self.estatura = min(max(normalvariate(EA_MU, EA_SIGMA), ESTATURA_MIN), ESTATURA_MAX)
        self.edad = 0


class Niño(Cliente):
    def __init__(self):
        self.estatura = min(max(normalvariate(EN_MU, EN_SIGMA), ESTATURA_MIN), ESTATURA_MAX)
        self.edad = 0
    


def Grupo():
    def __init__(self,adulto,niños=[]):
        self.adulto = adulto
        self.niños = niños



class Instalacion():
    """ """
    def __init__(self):
        pass

class Atraccion(Instalacion):
    """ """
    def __init__(self):
        pass

class Restaurant(Instalacion):
    """ """
    def __init__(self):
        pass


class Evento:
    def __init__(self,nombre,tiempo,Grupo=None):
        self.nombre = nombre
        self.tiempo = tiempo
        self.Grupo = Persona


    def __it__(self,other):
        if isnstance(other,Evento):
            return self.tiempo<other.tiempo
        return self.tiempo<other


if __name__ == '__main__':

    a=read_csv('arrivals.csv')
    for e in a:
        print(e)

    for i in range(5):
        fake = Faker()

        print(fake.name())