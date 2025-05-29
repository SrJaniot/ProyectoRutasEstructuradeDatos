# Sistema de Optimización de Rutas con Grafos

Este proyecto permite calcular rutas óptimas utilizando algoritmos de grafos sobre mapas geográficos. Es ideal para aplicaciones de logística, transporte y análisis de redes viales.



## Integrantes
- Esteban Francisco Janiot Rivera -2191593
- Santiago Moreno - 2221879
- Harold Peña - 2232733
- Juan David Alfonso perez -2232878

  
## Características

- Carga y visualización de mapas geográficos.
- Construcción de grafos a partir de datos espaciales.
- Cálculo de rutas óptimas usando algoritmos como Dijkstra.
- Visualización de rutas sobre el mapa.
- Soporte para diferentes formatos de datos geográficos.

## Requisitos

- Python 3.8 o superior

## Instalación

1. Clona el repositorio:
    ```bash
    git clone <URL-del-repositorio>
    cd grafo
    ```
2. Instala las dependencias:
    ```bash
    pip install geopandas contextily matplotlib networkx
    ```

## Uso

1. Ejecuta la aplicación principal:
    ```bash
    python main.py
    ```
2. Sigue las instrucciones en la terminal para cargar datos y calcular rutas.

## Estructura del Proyecto

```
grafo/
├── main.py
├── grafo.py
├── visualizacion.py
├── visualizacion_mapa.py
├── uis_edificios.csv
├── ubicaciones.csv
├── NODOS - COORDENADAS - DISTANCIAS.txt
├── README.md
└── __pycache__/
```



- **main.py**: Script principal para crear el grafo, calcular rutas y visualizar resultados.
- **grafo.py**: Implementación de la clase Grafo y algoritmos de rutas.
- **visualizacion.py**: Visualización simple del grafo.
- **visualizacion_mapa.py**: Visualización del grafo sobre un mapa real.
- **uis_edificios.csv**: Coordenadas de los nodos reales del campus UIS.
- **ubicaciones.csv**: Ejemplo de coordenadas para pruebas.
- **NODOS - COORDENADAS - DISTANCIAS.txt**: Documento de apoyo con nodos y distancias.




## Ejemplo de uso

Al ejecutar `main.py`, el sistema:
- Construye el grafo con los nodos y aristas definidos.
- Calcula las distancias mínimas desde un nodo origen usando Dijkstra.
- Calcula la matriz de distancias mínimas usando Floyd-Warshall.
- Muestra el camino más corto entre dos puntos específicos.
- Visualiza el grafo sobre el mapa usando los datos de `uis_edificios.csv`.



## Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para sugerencias o mejoras.

## Licencia

Este proyecto está bajo la licencia MIT.



## Galería de imágenes

| Imagen Base | Imagen Completa |
|-------------|----------------|
| ![Base](Imagen%20base.png) | ![Completa](Imagen%20completa.png) |

Otras visualizaciones:

![Visualización 2](Imagen%202.png)
![Visualización 3](Imagen%203.png)
![Visualización 4](Imagen%204.png)
![Visualización 5](Imagen%205.png)

