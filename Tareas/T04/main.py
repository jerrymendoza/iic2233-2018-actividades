import lib as lib
from params import *
from clases import *
ARRIVALS = "arrivals.csv"
class Parque():
	def __init__(self, tiempo_maximo):
		self.tiempo_maximo = tiempo_maximo
		self.tiempo_actual = 0
		self.eventos = list()
		self.grupos = list()
		self.capacidad_total = 100000 #formula para calcular en operador
		self.clientes_actuales= 0
		self.metodos = {'nuevo_grupo':self.nuevo_grupo }
		self.arrivals = lib.read_csv(ARRIVALS)

	def eventos_iniciales(self):
		"""Se inician los Juegos del Hambre"""
		self.entrada_grupos()
		
		#cargar eventos "llegan las personas, arrivals.csv"

	def entrada_grupos(self):
		cola = lib.read_csv(ARRIVALS)
		for i in cola:
			self.eventos.append(Evento('nuevo_grupo',lib.to_min(i.time)))

	def nuevo_grupo(self,*args):
		siguiente = next(self.arrivals)
		print("[Ingreso al Parque] {}".format(lib.to_hour(args[0].tiempo)))
		self.grupos.append(siguiente)

	def lluvia(self):
		"""Evento externo al parque:  Lluvia """
		pass
	def ruziland(self):
		"""Evento externo al parque:  Invasión Ruziland """
		pass
	def dia_colegio(self):
		"""Evento externo al parque:  Día colegio """
		pass



	def run(self):
		self.eventos_iniciales()
		while self.tiempo_actual <= self.tiempo_maximo and self.eventos:
			self.eventos.sort(key=lambda evento: evento.tiempo) #ocupar property
			evento = self.eventos.pop(0)
			if evento.tiempo < self.tiempo_maximo:
				self.tiempo_actual = evento.tiempo
				self.metodos[evento.nombre](evento)




if __name__ == '__main__':

	parque=Parque(100)
	parque.run()