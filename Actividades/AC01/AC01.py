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

class Alumno(Persona):
    def __init__(self):
        nivel_conocimiento = 10
        ramos=[]

    def estudiar(self):
        if nivel_conocimiento<100 and nivel_conocimiento>1:
            nivel_conocimiento += random.randrange(5,10)

        if nivel_conocimiento>100:
            nivel_conocimiento=100
        if nivel_conocimiento<1:
            nivel_conocimiento=1

    def __str__(self):
        return "{} {} \nRamos: {} \nNivel de Conocimiento {}".format(self.nombre, self.edad, self.ramos,str(self.nivel_conocimiento) )

class Profesor(Persona):
    def __init__(self,seccion):
        self.seccion = seccion

	def ensennar():
        pass

    def __str__(self):
        return "{} {}".format(self.nombre, self.edad)

class Ayudante(Alumno):
    def __init__(self,seccion):
        
        self.nivel_conocimiento = 75
        self.seccion = seccion
        

    def ensennar():
        pass

    def __str__(self):
        return "{} {}".format(self.nombre, self.edad)




a=Persona('Persona1','1/1/1995')