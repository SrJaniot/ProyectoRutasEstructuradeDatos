import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd  


def dibujar_grafo_en_mapa(grafo, archivo_ubicaciones):
    # Cargar coordenadas desde CSV
    df = pd.read_csv(archivo_ubicaciones)  
    gdf = gpd.GeoDataFrame(
        df, 
        geometry=gpd.points_from_xy(df.longitud, df.latitud),
        crs="EPSG:4326"  # Sistema de coordenadas WGS84 (lat/lon)
    )
    
    # Crear grafo de NetworkX
    G = nx.Graph() if not grafo.dirigido else nx.DiGraph()
    for nodo in grafo.nodos:
        for vecino, peso in grafo.nodos[nodo]:
            G.add_edge(nodo, vecino, weight=peso)
    
    # Dibujar el mapa base
    fig, ax = plt.subplots(figsize=(12, 10))
    gdf.plot(ax=ax, color="red", markersize=50, alpha=0.7)
    ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)
    
    # Dibujar el grafo
    pos = {nodo: (gdf[gdf.nodo == nodo].geometry.x.iloc[0], gdf[gdf.nodo == nodo].geometry.y.iloc[0]) for nodo in G.nodes}
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='skyblue', 
            node_size=200, font_size=8, font_weight='bold', 
            edge_color='gray', width=1.5)
    
    # Añadir etiquetas de pesos
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, ax=ax)
    
    plt.title("Optimización de Rutas sobre Mapa Real")
    plt.show()