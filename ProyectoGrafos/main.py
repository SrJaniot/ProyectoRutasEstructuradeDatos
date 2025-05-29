from grafo import Grafo
from visualizacion_mapa import dibujar_grafo_en_mapa

def main():
    # Crear grafo 
    red = Grafo(dirigido=False)


    # Agregar nodos y aristas
    red.agregar_arista("entrada_27", "1", 56.23)

    red.agregar_arista("1", "2", 112.75)

    red.agregar_arista("1", "auditorio", 48.74)

    red.agregar_arista("2", "entrada_30", 203.64)

    red.agregar_arista("2", "estadio_atletismo", 157.30)

    red.agregar_arista("entrada_30", "jardin_botanico", 178.22)

    red.agregar_arista("jardin_botanico", "3", 27.39)

    red.agregar_arista("3", "4", 164.79)

    red.agregar_arista("4", "5", 23.57)

    red.agregar_arista("5", "6", 87.27)

    red.agregar_arista("6", "7", 61.10)

    red.agregar_arista("7", "8", 15.59)

    red.agregar_arista("8", "9", 85.66)

    red.agregar_arista("9", "bienestar", 75.78)

    red.agregar_arista("9", "estadio_atletismo", 87.81)

    red.agregar_arista("bienestar", "11", 57.11)

    red.agregar_arista("11", "escuela_industrial", 37.76)

    red.agregar_arista("escuela_industrial", "18", 240.12)

    red.agregar_arista("11", "13", 50.96)

    red.agregar_arista("13", "14", 48.97)

    red.agregar_arista("14", "15", 40.70)

    red.agregar_arista("15", "16", 92.95)

    red.agregar_arista("16", "17", 62.30)

    red.agregar_arista("17", "18", 82.47)

    red.agregar_arista("18", "19", 85.77)

    red.agregar_arista("19", "20", 28.36)

    red.agregar_arista("20", "entrada_25", 98.49)

    red.agregar_arista("entrada_25", "21", 34.70)

    red.agregar_arista("21", "22", 201.03)

    red.agregar_arista("22", "23", 91.70)

    red.agregar_arista("23", "centic", 41.46)

    red.agregar_arista("23", "biblioteca", 28.38)

    red.agregar_arista("biblioteca", "26", 74.49)

    red.agregar_arista("26", "auditorio", 68.23)


        # Calcular y mostrar Dijkstra desde "A"
    print("Distancias mínimas desde entrada_27 (Dijkstra):")
    distancias_dijkstra = red.dijkstra("entrada_27")
    for nodo, distancia in distancias_dijkstra.items():
        print(f"A -> {nodo}: {distancia}")

    # Calcular y mostrar Floyd-Warshall
    print("\nMatriz de distancias mínimas (Floyd-Warshall):")
    distancias_fw = red.floyd_warshall()
    for origen in distancias_fw:
        for destino in distancias_fw[origen]:
            print(f"{origen} -> {destino}: {distancias_fw[origen][destino]}")
        print()
    
    
    
    
    distancia, camino = red.camino_minimo_dijkstra("centic", "escuela_industrial")
    print(f"Camino más corto de centic a escuela_industrial: {' -> '.join(camino)}")
    print(f"Distancia total: {distancia}")









    
    # Dibujar sobre mapa
    #dibujar_grafo_en_mapa(red, "ubicaciones.csv")
    dibujar_grafo_en_mapa(red, "uis_edificios.csv")




if __name__ == "__main__":
    main()