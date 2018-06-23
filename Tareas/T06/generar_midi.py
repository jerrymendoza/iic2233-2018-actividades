import lib

#chunk : type,length,data
#header: type->MThd, length -> 6,data ->formato,canales,ticks 

#HEADER
FORMATO = 1
CANALES = 1
TICKS = 160

#solo notas off  [tiempo,nota,intensidad]
notas = [[240,69,96]]

def crear_header():
	out = bytearray(b'MThd')
	out.extend((6).to_bytes(4,byteorder='big'))
	out.extend((FORMATO).to_bytes(2,byteorder='big'))
	out.extend((CANALES).to_bytes(2,byteorder='big'))
	out.extend((TICKS).to_bytes(2,byteorder='big'))

	return out


def crear_canal(notas):
	out = bytearray(b'MTrk')

	out2 = bytearray()
	for nota in notas:
		agregar_nota(out2,nota[0],nota[1],nota[2])

	agregar_fin(out2)
	print(len(out2))
	print((len(out2)).to_bytes(4,byteorder='big'))
	out.extend((len(out2)).to_bytes(4,byteorder='big'))
	out.extend(out2)
	#lenght out.extend((LARGOO).to_bytes(4,byteorder='big'))
	return out


def agregar_nota(array,tiempo,nota,intensidad):
	#notaON
	tiempo_on=lib.time_to_bytes(0)
	array.extend(tiempo_on)
	array.extend((144).to_bytes(1,byteorder='big'))
	array.extend((nota).to_bytes(1,byteorder='big'))
	array.extend((intensidad).to_bytes(1,byteorder='big'))


	#notaOFF
	tiempo_off=lib.time_to_bytes(tiempo)
	array.extend(tiempo_off)
	array.extend((128).to_bytes(1,byteorder='big'))
	array.extend((nota).to_bytes(1,byteorder='big'))
	array.extend((intensidad).to_bytes(1,byteorder='big'))




def agregar_fin(array):
	fin = [0,255,47,0]
	for i in fin:
		array.extend((i).to_bytes(1,byteorder='big'))





#CANAL
C_DATA = [{"tiempo": 0, "tipo": 144, "nota": 69, "intensidad": 96},
		  {"tiempo": 240, "tipo": 128, "nota": 69, "intensidad": 96}]

#print((FORMATO).to_bytes(2,byteorder='big'))
#print((CANALES).to_bytes(2,byteorder='big'))
#print((TICKS).to_bytes(2,byteorder='big'))


print(C_DATA)

aux=crear_header()
aux2=crear_canal(notas)

print(aux)
print(aux2)


