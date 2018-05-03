import funciones


class MetaAuto(type):
    contador=0
    def __new__(meta, nombre, base_clases, diccionario):
        diccionario["piezas"]=funciones.crear_piezas()
        diccionario["definir_estado_piezas"]=funciones.definir_estado_piezas
        return super().__new__(meta, nombre, base_clases, diccionario)
        
    
    def __init__(cls, nombre, base_clases, diccionario):
        cls.contador=0
        print(cls.contador)
        return super().__init__(nombre, base_clases, diccionario)


    def __call__(cls, *args, **kw):
        if cls.contador<3:  
            cls.contador+=1 
            print(cls.contador)
            cls.instance = super().__call__(*args, **kw)
            return cls.instance
        else:
            return None

class MetaTrabajador(type):
    def __new__(meta, nombre, base_clases, diccionario):
        del diccionario["revizar_ztado"]
        diccionario['revisar_estado']=funciones.revisar_estado
        diccionario['reparar']=funciones.reparar
     
        return super().__new__(meta, nombre, base_clases, diccionario)

    def __init__(cls, nombre, base_clases, diccionario):
        return super().__init__(nombre, base_clases, diccionario)

    def __call__(cls, *args, **kw):
        if not hasattr(cls, "instance"):
             cls.instance = super().__call__(*args, **kw)
        return cls.instance   

