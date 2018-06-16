import lib

PATH="Game of Throne.mid"



class Chunk:
	def __init__(self,tipo,length,data):
		self.type = tipo
		self.length = length
		self.data = data


with open(PATH,'rb') as file:
	a=file.read()
	a=bytearray(a)

	aux = a[0:14]
	aux2 =a[14:]
	print("HEADER")
	print(aux)
	print(aux[0:4])
	print(aux[4:8])
	print(int(aux[4:8].hex(),16))
	print(len(aux[8:]))

	print("CANAL")

	print(aux2)
	print(aux2[0:4])
	largo=int(aux2[4:8].hex(),16)
	print(largo)
	print(len(aux2[8:]))
	print(aux2[8:])
	print(aux2[8:largo+8])
	
	

	print("completo ---")
	print(aux2)


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


print((0).to_bytes(1, byteorder='big'))
print((255).to_bytes(1, byteorder='big'))
print((47).to_bytes(1, byteorder='big'))
print((0).to_bytes(1, byteorder='big'))