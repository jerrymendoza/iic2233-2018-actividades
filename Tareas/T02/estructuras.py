



class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0

    #ocupado para pruebas
    #def __repr__(self):
    #    return '[{}][{}]padre: {}, valor: {}'.format(self.clave,self.factorEquilibrio,self.padre, self.cargaUtil)
    def __repr__(self):
        return '{}: {}'.format(self.clave,self.cargaUtil)

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self


class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano


    def agregar(self,clave,valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1

    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                   self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                   nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                   self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                   nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)

    def __setitem__(self,c,v):
        if self.obtener(c) == None:
            self.agregar(c,v)
        else:
            nodoAEditar = self._obtener(c,self.raiz)
            nodoAEditar.cargaUtil=v
            

    def obtener(self,clave):
       if self.raiz:
           res = self._obtener(clave,self.raiz)
           if res:
                  return res.cargaUtil
           else:
                  return None
       else:
           return None

    def _obtener(self,clave,nodoActual):
       if not nodoActual:
           return None
       elif nodoActual.clave == clave:
           return nodoActual
       elif clave < nodoActual.clave:
           return self._obtener(clave,nodoActual.hijoIzquierdo)
       else:
           return self._obtener(clave,nodoActual.hijoDerecho)

    def __getitem__(self,clave):
       return self.obtener(clave)

    def __contains__(self,clave):
       if self._obtener(clave,self.raiz):
           return True
       else:
           return False

    def eliminar(self,clave):
      if self.tamano > 1:
         nodoAEliminar = self._obtener(clave,self.raiz)
         if nodoAEliminar:
             self.remover(nodoAEliminar)
             self.tamano = self.tamano-1
         else:
             raise KeyError('Error, la clave no está en el árbol')
      elif self.tamano == 1 and self.raiz.clave == clave:
         self.raiz = None
         self.tamano = self.tamano - 1
      else:
         raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self,clave):
       self.eliminar(clave)

    def empalmar(self):
       if self.esHoja():
           if self.esHijoIzquierdo():
                  self.padre.hijoIzquierdo = None
           else:
                  self.padre.hijoDerecho = None
       elif self.tieneAlgunHijo():
           if self.tieneHijoIzquierdo():
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoIzquierdo
                  else:
                     self.padre.hijoDerecho = self.hijoIzquierdo
                  self.hijoIzquierdo.padre = self.padre
           else:
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoDerecho
                  else:
                     self.padre.hijoDerecho = self.hijoDerecho
                  self.hijoDerecho.padre = self.padre

    def encontrarSucesor(self):
      suc = None
      if self.tieneHijoDerecho():
          suc = self.hijoDerecho.encontrarMin()
      else:
          if self.padre:
                 if self.esHijoIzquierdo():
                     suc = self.padre
                 else:
                     self.padre.hijoDerecho = None
                     suc = self.padre.encontrarSucesor()
                     self.padre.hijoDerecho = self
      return suc

    def encontrarMin(self):
      actual = self
      while actual.tieneHijoIzquierdo():
          actual = actual.hijoIzquierdo
      return actual

    def remover(self,nodoActual):
         if nodoActual.esHoja(): #hoja
           if nodoActual == nodoActual.padre.hijoIzquierdo:
               nodoActual.padre.hijoIzquierdo = None
           else:
               nodoActual.padre.hijoDerecho = None
         elif nodoActual.tieneAmbosHijos(): #interior
           suc = nodoActual.encontrarSucesor()
           suc.empalmar()
           nodoActual.clave = suc.clave
           nodoActual.cargaUtil = suc.cargaUtil

         else: # este nodo tiene un (1) hijo
           if nodoActual.tieneHijoIzquierdo():
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,
                                    nodoActual.hijoIzquierdo.cargaUtil,
                                    nodoActual.hijoIzquierdo.hijoIzquierdo,
                                    nodoActual.hijoIzquierdo.hijoDerecho)
           else:
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave,
                                    nodoActual.hijoDerecho.cargaUtil,
                                    nodoActual.hijoDerecho.hijoIzquierdo,
                                    nodoActual.hijoDerecho.hijoDerecho)

    def __repr__(self):
        def recorrer(nodo, lado="r"):
            ret = ''

            if nodo != None:
                #ret += '{0} -> {1}\n'.format(nodo, lado)
                ret += '{0}'.format(nodo)
                ret += recorrer(nodo.hijoIzquierdo, 'i')
                ret += recorrer(nodo.hijoDerecho, 'd')

            return ret

        ret = recorrer(self.raiz)
        return ret


class ArbolAVL(ArbolBinarioBusqueda):

    def __init__(self):
        ArbolBinarioBusqueda.__init__(self)

    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                    self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                    nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                    self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                    nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoDerecho)

    def actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                    nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                    nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(nodo.padre)

    def rotarIzquierda(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo

        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                    rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)

    def rotarDerecha(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo

        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho != None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                rotRaiz.padre.hijoDerecho = nuevaRaiz
            else:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio - 1 + min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio - 1 + max(rotRaiz.factorEquilibrio, 0)

    def reequilibrar(self,nodo):

        if nodo.factorEquilibrio < 0:
             if nodo.hijoDerecho.factorEquilibrio > 0:
                self.rotarDerecha(nodo.hijoDerecho)
                self.rotarIzquierda(nodo)
             else:
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
             if nodo.hijoIzquierdo.factorEquilibrio < 0:
                self.rotarIzquierda(nodo.hijoIzquierdo)
                self.rotarDerecha(nodo)
             else:
                self.rotarDerecha(nodo)

        def inorden(self,elemento):
            if elemento != None:
                self.inorden(elemento.hijoIzquierdo)
                yield elemento.cargaUtil
                self.inorden(elemento.hijoDerecho)
#Super listas
class ListaJ(ArbolAVL):
    def __init__(self):
        ArbolAVL.__init__(self)
        self.index=0

    def __init__(self,*args):
        ArbolAVL.__init__(self)
        self.index=0
        for i in args:
            self.append(i)

    def __repr__(self):
        aux=0
        salida="["
        while aux<self.index:
            if isinstance(self.__getitem__(aux), str):
                salida+="'{}'".format(self.__getitem__(aux))
            else:
                salida+=str(self.__getitem__(aux))
            aux+=1
            if not aux==self.index:
                salida+=","
        salida+="]"
        return salida

    def getRaiz(self):
        return self.raiz

    #probando probando
    def inorden(self,elemento):
        if elemento != None:
            yield from self.inorden(elemento.hijoIzquierdo)
            yield elemento.cargaUtil
            yield from self.inorden(elemento.hijoDerecho)

    def existe_valor(self,valor):
        aux=0
        nodo_actual = self[aux]
        while not nodo_actual == None:
            if nodo_actual==valor:
                return True
            aux+=1
            nodo_actual = self[aux]
        return False

    def append(self, value):
        self.__setitem__(self.index,value)
        self.index+=1


    def sort(self):
        pass

    def __iter__(self):
        return self.inorden(self.raiz)

class ListaNoLinealJ(ArbolAVL):
    def __init__(self):
        ArbolAVL.__init__(self)

    def inorden(self,elemento):
        if elemento != None:
            yield from self.inorden(elemento.hijoIzquierdo)
            yield elemento.cargaUtil
            yield from self.inorden(elemento.hijoDerecho)

    def __iter__(self):
        return self.inorden(self.raiz)
         
    def getRaiz(self):
        return self.raiz

class ListaNoLinealJ2(ListaNoLinealJ):
    def __init__(self):
        ListaNoLinealJ.__init__(self)

    def inorden(self,elemento):
        if elemento != None:
            yield from self.inorden(elemento.hijoIzquierdo)
            yield elemento
            yield from self.inorden(elemento.hijoDerecho)        


class Grafo:
    def __init__(self):
        self.lista =  ListaNoLinealJ2()
        #lista[origen] = [[destino,peso],[destino2,peso2]...]

    def _agregar_vertice(self,id):
        if not self.lista[id]:
            self.lista[id]=ListaJ()


    def agregar_arista(self,origen_id,destino_id,peso):
        self._agregar_vertice(origen_id)
        self._agregar_vertice(destino_id)
        if not self.existe_arista(origen_id,destino_id) and not self.existe_arista(destino_id,origen_id):
            self.lista[origen_id].append(ListaJ(destino_id,peso))
            self.lista[destino_id].append(ListaJ(origen_id,peso))

    def existe_arista(self,origen_id,destino_id):
        if not self.lista[origen_id]==None:
            for destino in self.lista[origen_id]:
                if destino[0]==destino_id:
                    return True
                    print("existeeeee")
        return False


    def mas_popular(self):
        ide=0
        largo=0
        for i in self.lista:
            if len(i.cargaUtil)>largo:
                ide=i.clave
                largo=len(i.cargaUtil)
        return ide

    

    #probar
    def imp(self):
        for i in self.lista:
            print(i.clave)
            print(i.cargaUtil)



if __name__ == "__main__":

    #miArbol = ArbolBinarioBusqueda()
    #miArbol["a"]="aa que tal"

    #miArbol["c"]="cc qu222 tal"
    #miArbol["b"]="bb que tal"
    #miArbol["z"]="zzz que tal"
    #miArbol["l"]="ll que tal"
    #miArbol["y"]="ll que tal"


    #print(miArbol)
    #print("asdfsdsdf")
    #print(miArbol["a"])



    #miArbol2 = ArbolAVL()
    #miArbol2["a"]="aa que tal"

    #miArbol2["c"]="cc qu222 tal"
    #miArbol2["b"]="bb que tal"
    #miArbol2["z"]="zzz que tal"
    #miArbol2["l"]="ll que tal"
    #miArbol2["y"]="ll que tal"


    #print(miArbol2)
    #print("asdfsdsdf")
    #print(miArbol2["a"])

    #miArbol3 = ListaJ()
    #miArbol3.append("aa que tal")
    #miArbol3.append("cc qu222 tal")
    #miArbol3.append("bb que tall")
    #miArbol3.append("ll que tal")
    #miArbol3.append("yy que tal")


    #print(miArbol3)
    #print("asdfsdsdf")
    #print(miArbol3[0])
    #print(miArbol3[4])

    #miArbol4=ListaJ(324,346,865443,"hola",987243,True)
    #print("---------")
    #print("como lista:")
    #print(miArbol4)
    #print("---------")
    #miArbol4[0]="cambie estooo"
    #print(miArbol4)
    #print("---------")
    #print("---------")
    #print("---------")
    #for i in miArbol4:
    #    print(i)


    graf=Grafo()
    #agregar_arista(origen,destino,peso)
    graf.agregar_arista(1,2,31)
    graf.agregar_arista(2,3,40)
    graf.agregar_arista(3,8,69)

    graf.imp()