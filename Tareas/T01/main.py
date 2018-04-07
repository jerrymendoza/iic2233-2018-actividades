from datetime import datetime
from lib import read_csv 
from misclases import Galaxia,Maestro,Aprendiz,Asesino


planeta1 = Maestro("uno")
print(planeta1.soldados)
planeta1.soldados = 10
print(planeta1.soldados)
planeta1.magos = 101
print(planeta1.magos)
planeta1.magos = 90
print(planeta1.magos)





#print(read_csv("planetas.csv","planeta"))

#print(read_csv("galaxias.csv","galaxia"))


print("{} GALAXIANEITOR 3000 {}".format("*"*20,"*"*20).center(80))

print("     (1) Crear Galaxia")
print("     (2) Modificar una Galaxia")
print("     (3) Consultar sobre una Galaxia")
print("     (4) Jugar en una Galaxia")

input("\nOpcion: ")