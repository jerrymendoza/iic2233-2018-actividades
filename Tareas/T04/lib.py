import csv
from collections import namedtuple


def read_csv(path):
    with open(path, newline="") as file:
        reader = csv.reader(file, skipinitialspace=True)
        Data = namedtuple("Data", next(reader))
        for row in reader:
            yield Data(*list(row))


def to_min(hora_en_string):
	"""Recibe hora en string 00:00 y retorna un int
	   de minutos DESDE las 10:00
	   Asi las 10:15 -> 15
	"""
	horas,minutos = hora_en_string.strip().split(":")
	horas = int(horas)-10
	minutos = int(minutos)
	return horas*60+minutos


def to_hour(numero):
	"""Recibe un int y retorna la hora en string con
	   la hora correspondiente
	   Asi 15 -> 10:15
	"""
	minutos = numero%60
	horas = int((numero-minutos)/60)+10

	return "{}:{}".format(horas,minutos)


if __name__ == '__main__':

	print("to-min")
	print(to_min("10:59"))

	print("to-hour")
	print(to_hour(59))