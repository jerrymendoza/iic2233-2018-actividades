import collections

def bytes_to_time(bytes):
	l = []
	array = bytearray(bytes)
	for byte in array:
		l.append(byte)

	for i in range(len(l)):
		l[i] = int(bin(l[i])[2:][-7:])

	binario = "".join(map(str,l))
	return int(binario,2)


def time_to_bytes(time):
	b = bin(time)[2:]
	#print(b)
	de_7 = []
	de_7.append(b[-7:])
	multi=2
	if len(b)>7:
		while True:
			inicio=-7*multi
			final=-7*multi+7 
			de_7.append(b[inicio:final])
			multi+=1
			if -inicio>=len(b):
				break
	de_7 = list(map(lambda x: x.zfill(7), de_7))
	add = '0'
	for i in range(len(de_7)):
		de_7[i]=add+de_7[i]
		add = '1'
	de_7 = de_7[::-1]
	de_7 = list(map(lambda x: int(x,2).to_bytes(1, byteorder='big'), de_7))
	final = b''.join(de_7)
	#print(de_7)
	return final


def leer_notas(array):
    while True:
        if array.count(b'\x90')>0 and array.count(b'\x80')>0:
            type_index = min(array.index(b'\x90'),array.index(b'\x80'))
        elif array.count(b'\x90')==0 and array.count(b'\x80')>0:
            type_index = array.index(b'\x80')
        elif array.count(b'\x80')==0 and array.count(b'\x90')>0:
            #esto no deberia ocurrir nunca
            type_index = array.index(b'\x90') 
        else:
            type_index = None

        if type_index != None:
            tiempo = bytearray()
            for _ in range(type_index):
                tiempo.append(array.pop(0))  
            #data = collections.OrderedDict()
            data = {}
            data["tiempo"] = bytes_to_time(tiempo)
            data["tipo"] = array.pop(0)
            data["nota"] = array.pop(0)
            data["intensidad"] = array.pop(0)

            yield data
            #print("tiempo: {}".format(lib.bytes_to_time(tiempo)))
            #print("tipo: {}".format(array.pop(0)))
            #print("nota: {}".format(array.pop(0)))
            #print("intensidad: {} \n".format(array.pop(0)))
        else:
            break

if __name__ == '__main__':
	
	print(time_to_bytes(320))
	print(bytes_to_time(b'\x82@'))

	print(bytes_to_time(b'\x00'))
