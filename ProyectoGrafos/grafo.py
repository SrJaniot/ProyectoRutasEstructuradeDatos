# grafo/grafo.py
import heapq

class Grafo:
    """
    Clase para representar un grafo (dirigido o no) usando listas de adyacencia.
    """
    def __init__(self, dirigido=False):
        self.nodos = {}  # {nodo: [(vecino, peso), ...]}
        self.dirigido = dirigido

    def agregar_nodo(self, nodo):
        if nodo not in self.nodos:
            self.nodos[nodo] = []

    def agregar_arista(self, inicio, fin, peso=1):
        self.agregar_nodo(inicio)
        self.agregar_nodo(fin)
        self.nodos[inicio].append((fin, peso))
        if not self.dirigido:
            self.nodos[fin].append((inicio, peso))

    def dijkstra(self, inicio):
        distancias = {nodo: float('inf') for nodo in self.nodos}
        distancias[inicio] = 0
        cola = [(0, inicio)]
        visitados = set()

        while cola:
            distancia_actual, nodo_actual = heapq.heappop(cola)
            if nodo_actual in visitados:
                continue
            visitados.add(nodo_actual)

            for vecino, peso in self.nodos[nodo_actual]:
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola, (distancia, vecino))
        return distancias

    def floyd_warshall(self):
        distancias = {nodo: {v: float('inf') for v in self.nodos} for nodo in self.nodos}
        for nodo in self.nodos:
            distancias[nodo][nodo] = 0
            for vecino, peso in self.nodos[nodo]:
                distancias[nodo][vecino] = peso

        for k in self.nodos:
            for i in self.nodos:
                for j in self.nodos:
                    distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])
        return distancias
    
    






    def camino_minimo_dijkstra(self, inicio, fin):
        import heapq
        distancias = {nodo: float('inf') for nodo in self.nodos}
        anteriores = {nodo: None for nodo in self.nodos}
        distancias[inicio] = 0
        cola = [(0, inicio)]
        visitados = set()

        while cola:
            distancia_actual, nodo_actual = heapq.heappop(cola)
            if nodo_actual in visitados:
                continue
            visitados.add(nodo_actual)
            if nodo_actual == fin:
                break
            for vecino, peso in self.nodos[nodo_actual]:
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    anteriores[vecino] = nodo_actual
                    heapq.heappush(cola, (distancia, vecino))

        # Reconstruir el camino
        camino = []
        actual = fin
        while actual is not None:
            camino.insert(0, actual)
            actual = anteriores[actual]
        if distancias[fin] == float('inf'):
            return float('inf'), []  # No hay camino
        return distancias[fin], camino