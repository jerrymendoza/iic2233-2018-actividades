from lib import read_csv 
from misclases import Galaxia,Maestro,Aprendiz,Asesino


planeta1 = Maestro("uno",tasa_minerales=20,soldados=30)
print(planeta1.soldados)
planeta1.soldados = 10
print(planeta1.soldados)
planeta1.magos = 101
print(planeta1.magos)
planeta1.magos = 90
print(planeta1.magos)
print("tasa:")
print(planeta1.tasa_minerales)


#print(read_csv("planetas.csv","planeta"))

#print(read_csv("galaxias.csv","galaxia"))
galaxias=[]

print("{} ChauCraft {}".format("*"*20,"*"*20).center(80))

print("     (0) Cargar Archivos csv")
print("     (1) Crear Galaxia")
print("     (2) Modificar una Galaxia")
print("     (3) Consultar sobre una Galaxia")
print("     (4) Jugar en una Galaxia")

input("\nOpcion: ")

print("(1) Crear Galaxia =>")
nombre_galaxia=input("Nombre para la Galaxia nueva: ")

galaxias.append(Galaxia(nombre_galaxia))

for i in galaxias:
    print(i)