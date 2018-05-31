import os
current=os.getcwd()
def buscar_paths(path):
    archivos = []
    for dirpath, subdirs, files in os.walk(path):
        for x in files:
            if x.endswith("marciano64.png") or x.endswith("marcianozurdo.pep") :
                archivos.append(os.path.join(dirpath, x))

    dic={}
    for i in archivos:
        if i.endswith("marciano64.png"):
            dic["png"] = i
        if i.endswith("marcianozurdo.pep"):
            dic["pep"] = i
    return dic

paths=buscar_paths(current)

def funcion1(paths):
    base64="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    cadena=""
    with open(paths['png'], 'rb') as f:
        a=f.read()
        for x in a:
            aux=chr(x)
            aux2=base64.index(aux)
            aux3=bin(aux2)[2:]
            aux4=aux3.zfill(6)
            cadena+=str(aux4)

    de8en8 = [cadena[i:i+8] for i in range(0, len(cadena), 8)]

    bit_list=bytearray()
    for cha in de8en8:
        bit_list.append(int(cha,2))

    return bit_list

def funcion2(chunk):
    total = bytearray(chunk[1:])
    total.append(chunk[0])
    return total


def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def final(paths):
    i=0
    total=bytearray()
    png = funcion1(paths)
    fibo=fib()
    with open(paths['pep'], 'rb') as f:
        pep=f.read()

    while pep or png:
        siguiente=next(fibo)
        if i % 2 == 0:
            salida = pep[:siguiente]
            pep = pep[siguiente:]
            total.extend(funcion2(salida))
        else:
           salida =png[:siguiente]
           png = png[siguiente:] 
           total.extend(salida)
        i += 1
    with open("resultado.png","wb") as f:
        f.write(total)
         
        

final(paths)