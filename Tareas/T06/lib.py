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

if __name__ == '__main__':
	
	print(time_to_bytes(320))
	print(bytes_to_time(b'\x82@'))

	print(bytes_to_time(b'\x00'))
