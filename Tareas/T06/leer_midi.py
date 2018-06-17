import lib

PATH="Game of Throne.mid"

class Chunk:
	def __init__(self,tipo,length,data):
		self.type = tipo
		self.length = length
		self.data = data


def mensaje(array):
	while True:
		try:
			type_index = min(array.index(b'\x90'),array.index(b'\x80'))
		except ValueError:
			type_index = None

		if type_index != None:
			tiempo = bytearray()
			for _ in range(type_index):
				tiempo.append(array.pop(0))  
				
			print("tiempo: {}".format(lib.bytes_to_time(tiempo)))
			print("tipo: {}".format(array.pop(0)))
			print("nota: {}".format(array.pop(0)))
			print("intensidad: {} \n".format(array.pop(0)))
		else:
			break

with open(PATH,'rb') as file:
	a=file.read()
	a=bytearray(a)

	aux = a[0:14]
	aux2 =a[14:]
	print("------ HEADER ------")
	print(aux)
	print("    Type HEADER:")
	#print(aux[0:4]) #'MThd'
	print(aux[0:4].decode("ascii"))
	print("    Largo HEADER:")
	#print(aux[4:8])
	print(int(aux[4:8].hex(),16)) #data header
	print("    Data HEADER:")
	data_header=aux[8:]
	print(int(data_header[0:2].hex(),16))
	print(int(data_header[2:4].hex(),16))
	print(int(data_header[4:].hex(),16))
	print("------ CANAL ------")
	print(aux2)

	print("    Header CANAL")
	print(aux2[0:4].decode("ascii")) #'MTrk'

	print("    Largo CANAL:")
	largo=int(aux2[4:8].hex(),16)
	print(largo)
	print(len(aux2[8:]))

	print("    Data CANAL:")
	data_canal=aux2[8:largo+8]
	print(data_canal)
	print(data_canal.index(b'\x90'))
	print(data_canal.index(b'\x80'))
	mensaje(data_canal)
	print(data_canal.index(b'\x90'))
	print(data_canal)
	print("---")
	



	


print("ESTO NO, FINAL")
test1=bytearray(b'\x00\xff/\x00')
print(test1[0:2])
print(test1[2:3])
for i in test1:
	print(i)


def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result

