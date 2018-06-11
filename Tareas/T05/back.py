BOMBAS_ACTIVAS = 1
VIDAS = 3
PLAYER_SPEED            = 12
N = 48 #pixeles,no midificar

def leer_mapa(path):
    retornar=list()
    with open(path, 'r') as file:
        for linea in file:
            retornar.append(linea.strip().split())
    return retornar


class Mapa():
    def __init__(self,path):
        posiciones = leer_mapa(path)
        self.tamano = (0,0)
        self.bombas = [] 
        self.destructibles = [] #(x,y) (0 -> 14)
        self.indestructibles = [] #(x,y)
        self._constructor(posiciones)

    def _constructor(self,posiciones):
        self.tamano = (len(posiciones[0]),len(posiciones))
        for y in range(len(posiciones)):
            for x in range(len(posiciones[y])):
                if posiciones[y][x] == "X":
                    self.indestructibles.append((x,y))
                elif posiciones[y][x] == "P":
                    self.destructibles.append((x,y))
        print(self.indestructibles)

    def mov_valido(self,destino):
        #destino (x,y)
        x=int(destino[0])//N
        y=int(destino[1])//N


        dx=int(destino[0])%N
        dy=int(destino[1])%N
        print("----")
        print(x,y)

        
        

        print("----")
        print(destino)
        print(x,y)
        print(dx,dy)
        if ((x,y) in self.indestructibles or
            (x,y) in self.destructibles or
            (x,y) in self.bombas
            ):

            return False

        
        valido=True
       




        return valido


class Elemento():

    def __init__(self, x, y):
        self.y = y
        self.x = x



class Player(Elemento):

    def __init__(self, x, y):
        Elemento.__init__(self, x, y)
        self.num_bombas = BOMBAS_ACTIVAS
        self.vidas = VIDAS
        self.puntaje = 0

    def dejar_bomba(self):
        if self.num_bombas > 0:
            Bomba(self)
            self.num_bombas -= 1



class Bomba(Elemento):

    def __init__(self, player):
        Elemento.__init__(self, player.x, player.y)
        self.player = player
        self.radio = 3

    def explotar(self):
        #hacer que haga algo


        self.player.num_bombas += 1
   
def guardar(item):
    with open('ranking.txt', 'a') as file:
        file.write(",".join(item)+"\n")

def ranking():
    lista=[]
    with open('ranking.txt','r') as file:
        for line in file:
            aux=line.strip().split(",")
            lista.append((aux[0],aux[1]))
    return lista



if __name__ == '__main__':
    
    print(leer_mapa("mapa.txt"))

