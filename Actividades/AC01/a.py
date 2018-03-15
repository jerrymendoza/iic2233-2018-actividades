import random
class Persona:
    rut=0
    def __init__(self, nombre, fecha_nacimiento):
        self.rut = Persona.rut
        Persona.rut +=1
        self.nombre = nombre
        self.f_nacimiento=date(fecha_nacimiento) #dia/mes/anno

	def edad(self):
        a=0
        #calcular edad
        return str(a)

    def __str__(self):
        return "{} {}".format(self.nombre, self.edad)
    

class Alumno(Persona):
    def __init__(self):
        nivel_conocimiento = 10
        ramos=[]

    def estudiar(self):
        nivel_conocimiento += random.randrange(5,10)
        

class Profesor(Persona):
    def __init__(self,seccion):
        self.seccion = seccion

	def ensennar():
        pass

    def __str__(self):
        return "{} {}".format(self.nombre, self.edad)

class Ayudante(Alumno):
    def __init__(self,seccion):
        self.seccion = seccion
        self.nivel_conocimiento = 75

    def ensennar():
        pass

    def __str__(self):
        return "{} {}".format(self.nombre, self.edad)


