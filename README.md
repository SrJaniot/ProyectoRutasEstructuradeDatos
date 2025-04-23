# ProyectoRutasEstructuradeDatos

# Rutas con Árboles 

Esta aplicación permite gestionar rutas entre ciudades en Colombia usando una estructura de árbol. Utiliza la librería `bigtree` para representar la jerarquía y `tkinter` para la interfaz gráfica.


## Integrantes
- Esteban Francisco Janiot Rivera -2191593
- Santiago Moreno - 2221879



##  Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instalado Python 3.7 o superior y los siguientes paquetes:

- `bigtree`: Para la estructura de árbol.
- `tkinter`: Viene preinstalado con Python en la mayoría de distribuciones.

##  Instalación

1. **Clona o descarga este repositorio.**

2. **Instala las dependencias necesarias:**

```bash
pip install bigtree
```

3. **Ejecuta la aplicación:**

```bash
python RutasConArbolesGUI.py
```

##  Uso

1. **Agregar una ruta:**
   - Ingresa una ciudad de **origen** y una de **destino**.
   - Haz clic en **Agregar Ruta**.

2. **Consultar si existe una ruta:**
   - Selecciona una ciudad de **origen** y una de **destino** desde los menús desplegables.
   - Haz clic en **Consultar Ruta**.

3. **Visualizar la estructura del árbol:**
   - Presiona el botón **Visualizar Árbol (Consola)** para ver la jerarquía de rutas en la consola.

##  Ejemplo de árbol

Si agregas estas rutas:
- Bogotá → Medellín  
- Medellín → Cali

La estructura impresa en consola será:

```
Colombia
└── Bogotá
    └── Medellín
        └── Cali
```

##  Notas

- Todas las ciudades están conectadas jerárquicamente bajo la raíz "Colombia".
- Puedes visualizar el árbol actualizado en cualquier momento con el botón correspondiente.
