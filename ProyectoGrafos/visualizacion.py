import networkx as nx
import matplotlib.pyplot as plt

def dibujar_grafo(grafo):
    G = nx.Graph() if not grafo.dirigido else nx.DiGraph()
    for nodo in grafo.nodos:
        for vecino, peso in grafo.nodos[nodo]:
            G.add_edge(nodo, vecino, weight=peso)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', 
            node_size=800, font_weight='bold', font_size=10)
    nx.draw_networkx_edge_labels(G, pos, 
                                edge_labels={(u, v): d['weight'] 
                                for u, v, d in G.edges(data=True)})
    plt.title("Red de Transporte")
    plt.show()