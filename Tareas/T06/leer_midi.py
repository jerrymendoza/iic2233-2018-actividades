import lib
import json




PATH="Game of Throne.mid"

class Chunk:
    def __init__(self,tipo,length,data):
        self.type = tipo
        self.length = length
        self.data = data




with open(PATH,'rb') as file:
    datos = {}
    datos['header'] = {}
    datos['canal'] = {}
    a=file.read()
    a=bytearray(a)
    aux = a[0:14]
    aux2 =a[14:]
    print("------ HEADER ------")
    print(aux)
    #print("    Type HEADER:")
    #print(aux[0:4]) #'MThd'
    datos['header']['type']=aux[0:4].decode("ascii")
    #print(aux[0:4].decode("ascii"))
    #print("    Largo HEADER:")
    #print(aux[4:8])
    datos['header']['length'] = int(aux[4:8].hex(),16)
    #print(int(aux[4:8].hex(),16)) #data header
    #print("    Data HEADER:")
    data_header=aux[8:]
    datos['header']['data'] = {}
    datos['header']['data']['formato'] = int(data_header[0:2].hex(),16)
    #print(int(data_header[0:2].hex(),16))
    datos['header']['data']['canales'] = int(data_header[2:4].hex(),16)
    #print(int(data_header[2:4].hex(),16))
    datos['header']['data']['ticks'] = int(data_header[4:].hex(),16)
    #print(int(data_header[4:].hex(),16))




    
    #print("------ CANAL ------")
    #print(aux2)

    #print("    type CANAL")
    datos['canal']['type'] = aux2[0:4].decode("ascii") 
    #print(aux2[0:4].decode("ascii")) #'MTrk'

    #print("    Largo CANAL:")
    largo=int(aux2[4:8].hex(),16)
    datos['canal']['length'] = largo 
    #print(len(aux2[8:]))

    #print("    Data CANAL:")
    data_canal=aux2[8:largo+8]
    print(data_canal)
    datos['canal']['data'] = []
    notas = lib.leer_notas(data_canal)
    for i in notas:
        datos['canal']['data'].append(i)

    datos['canal']['data'].append({'end': [0,255,47,0]})


    print("resultado:")
    #print(json.dumps(datos, indent=3)) #SACAAAARR
    print(data_canal)
    print("---")
    



    



#final=bytearray(b'\x00\xff/\x00')


