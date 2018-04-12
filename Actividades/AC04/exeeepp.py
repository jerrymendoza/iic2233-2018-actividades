class dateException(Exception):
    def __init__(self):
       super().__init__("Fecha no valida")

class nException(Exception):
    def __init__(self,n):
       super().__init__("{} no son digitos".format(n))



def probar(date):
    if not date[0:1].isdigit() and date[3:4].isdigit() and date[6:7].isdigit() and date[2]=="." and date[5]==".":
      	raise dateException()

def digitos(n):
    if not n.isdigit():
        raise nException(n)