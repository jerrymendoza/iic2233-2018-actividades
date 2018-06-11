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

        #if dx>=36:
        #    x+=1
        #if dy>=36:
        #    y+=1

        if ((x,y) in self.indestructibles or
            (x,y) in self.destructibles or
            (x,y) in self.bombas
            ):

            return False

        #print(self.indestructibles)
        #dentro del tablero
        #if x<0 or x>15*N:
        #   return False
        #if y<0 or y>15*N:
        #   return False
        valido=True
        #for i in self.indestructibles:
            #48,48
        #   if (x>=i[0]*N and x<=i[0]*(N+1)) or (y>=i[1]*N and y<=i[1]*(N+1)):
        #       valido = False




        return valido


class Elemento():

    def __init__(self, y, x):
        self.y = y
        self.x = x



class Player(Elemento):

    def __init__(self, y, x):
        Elemento.__init__(self, y, x)
        self.num_bombas = BOMBAS_ACTIVAS
        self.vidas = VIDAS

    def dejar_bomba(self):
        if self.num_bombas > 0:
            Bomba(self)
            self.num_bombas -= 1



class Bomba(Elemento):

    def __init__(self, player):
        Elemento.__init__(self, player.y, player.x)
        self.player = player
        self.radio = 3

    def explotar(self):
        #hacer que haga algo


        self.player.num_bombas += 1
   



if __name__ == '__main__':
    
    print(leer_mapa("mapa.txt"))

