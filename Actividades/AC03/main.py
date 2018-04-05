class GraphNode:
    def __init__(self, nombre):
        self.nombre = nombre
        self.destino = []

    def agregar_destino(self,destino):
        self.destino.append(destino)


class Graph:
    def __init__(self):
        self.nodos = []
        
    def cargar_archivo(self, path_archivo):
        with open(path_archivo,"r") as f:
            for linea in f:
                origen,destino = linea.strip().split(',')
                self.agregar_conexion(origen,destino)
        

    def agregar_conexion(self, origen, destino):
        for i in self.nodos:
            if i.nombre == origen:
                i.agregar_destino(destino)
                break
        else: 
            nodo = GraphNode(origen)
            self.nodos.append(nodo)
            for i in self.nodos:
                if i.nombre == origen:
                    i.agregar_destino(destino)

    def quitar_conexion(self, origen, destino):
        for i in self.nodos:
            if i.nombre == origen:
                if destino in i.destino:
                    i.destino.remove(destino)
                break

    def encontrar_camino(self, origen, destino):
        
        for i in self.nodos:
            if i.nombre == origen:
                if destino in i.destino:
                    return True
                else:
                    for e in i.destino:
                        return self.encontrar_camino(e,destino)

        return False

    def encontrar_camino_corto(self, origen, destino):
        return ''

    def export_csv(self, path_archivo):
        s=""
        for i in self.nodos:
            for e in i.destino:
                s +=  "{},{}\n".format(i.nombre,e)
        with open(path_archivo,'w') as f:
            f.write(s)


if __name__ == "__main__":
    print("*" * 20 + "EASY" + "*" * 20)
    grafo_facil = Graph()
    grafo_facil.cargar_archivo("easy.txt")
    print(grafo_facil.encontrar_camino("A", "C"))  # True
    print(grafo_facil.encontrar_camino("B", "A"))  # False
    print(grafo_facil.encontrar_camino_corto("A", "E"))  # [A, B, E]
    print(grafo_facil.encontrar_camino_corto("A", "C"))  # [A, C]
    grafo_facil.quitar_conexion("A", "C")
    print(grafo_facil.encontrar_camino("A", "C"))  # True
    print(grafo_facil.encontrar_camino_corto("A", "C"))  # [A, B, E, C]
    grafo_facil.quitar_conexion("B", "E")
    print(grafo_facil.encontrar_camino("A", "C"))  # True
    print(grafo_facil.encontrar_camino_corto("A", "C"))  # [A, B, D, E, C]
    grafo_facil.quitar_conexion("D", "E")
    print(grafo_facil.encontrar_camino("A", "C"))  # False
    grafo_facil.agregar_conexion("A", "C")
    print(grafo_facil.encontrar_camino("A", "C"))  # True
    grafo_facil.export_csv("easy_output.txt")  # A,B
                                               # A,C
                                               # B,D
                                               # E,C

    print("\n" + "*" * 20 + "MEDIUM" + "*" * 20)
    grafo_medium = Graph()
    grafo_medium.cargar_archivo("medium.txt")
    print(grafo_medium.encontrar_camino("A", "G"))  # True
    print(grafo_medium.encontrar_camino("A", "D"))  # True
    print(grafo_medium.encontrar_camino_corto("A", "G"))  # [A, F, G]
    grafo_medium.quitar_conexion("A", "F")
    grafo_medium.quitar_conexion("A", "I")
    grafo_medium.quitar_conexion("A", "M")
    grafo_medium.quitar_conexion("A", "D")
    grafo_medium.quitar_conexion("A", "E")
    print(grafo_medium.encontrar_camino("A", "G"))  # False

    print("\n" + "*" * 20 + "HARD" + "*" * 20)
    grafo_hard = Graph()
    grafo_hard.cargar_archivo("hard.txt")
    print(grafo_hard.encontrar_camino_corto("A", "Z"))  # [A, 0, 4, 5, L, Z]
    print(grafo_hard.encontrar_camino("A", "G"))  # True
    grafo_hard.agregar_conexion("4", "Z")
    print(grafo_hard.encontrar_camino_corto("A", "Z"))  # [A, 0, 4, Z]
    grafo_hard.quitar_conexion("4", "Z")
    print(grafo_hard.encontrar_camino_corto("A", "Z"))  # [A, 0, 4, 5, L, Z]
    print(grafo_hard.encontrar_camino("X", "Z"))  # False
    grafo_hard.agregar_conexion("X", "B")
    print(grafo_hard.encontrar_camino("X", "Z"))  # True
    print(grafo_hard.encontrar_camino_corto("X", "Z"))  # [X, B, T, L, Z]
