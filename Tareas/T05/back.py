def leer_mapa(path):
	retornar=list()
	with open(path, 'r') as file:
		for linea in file:
			retornar.append(linea.strip().split())
	return retornar


class Personaje():
	def __init__(self):
		self.posicion=(0,0)
		self._vidas=3



class Mapa():
	def __init__(self,path):
		posiciones = leer_mapa(path)
		self.tamano = (0,0)
		self.bombas = []
		self.destructibles = [] #(x,y)
		self.indestructibles = [] #(x,y)
		self._constructor(posiciones)

	def _constructor(self,posiciones):
		self.tamano = (len(posiciones[0]),len(posiciones))
		for y in range(len(posiciones)):
			for x in range(len(posiciones[y])):
				if posiciones[y][x] == "X":
					self.indestructibles.append((x,y))
				elif posiciones[y][x] == "P":
					self.destructibles.append((x,y))







class Enemigo():
	def __init__(self):
		self.posicion=(0,0)
		pass



if __name__ == '__main__':
	
	print(leer_mapa("mapa.txt"))

