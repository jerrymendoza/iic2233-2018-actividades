from itertools import count
import math

class Evento:
	"""docstring for Evento"""
	ids = count(start=0)
	def __init__(self,tiempo,funcion):
		self.id = id
		self.tiempo = tiempo
		self.funcion = funcion

	def __it__(self,other):
		if isnstance(other,Evento):
			return self.tiempo<other.tiempo
		return self.tiempo<other

class MotorSimulacion:
	def __init__(self,tiempo_inicio,tiempo_fin=math.inf):
		self._tiempo_simulacion = tiempo_inicio
		self._tiempo_fin=tiempo_fin
		self._eventos=[]

	def agregar_evento(self, evento):
		self.eventos.append(evento)

	@property
	def eventos(self):
		self._eventos.sort()
		return self._eventos

	@property
	def tiempo_fin(self):
		return self._tiempo_fin

	@property
	def tiempo_simulacion(self):
		return self._tiempo_simulacion


	def run(self):
		while self.eventos and self.eventos[0] < self.tiempo_fin:
			evento =self.eventos.pop()
			self._tiempo_simulacion = evento.tiempo_fin
			print("_"*80)
			print("TIEMPO: {:.2f}".format(self.tiempo_simulacion))
			evento.funcion()


class ObjetoSimulacion:
	def __init__(self,motor_simulacion,*args,*kwargs):
		self.motor_simulacion motor_simulacion
		self.configurar()

	def configurar(self):
		evento = Evento(15,lambda : print("Evento de saludar"))
		self.motor_simulacion.agregar_evento(evento)

	def imprimir_estadisticas(self):
		print("aca iria algo relevante!")

class MiSimulacion:
	def __init__(self):
		self.motor = MotorSimulacion(tiempo_fin=500)
		self.objeto = ObjetosSimulacion(self.motor)



		