import tkinter as tk
from tkinter import ttk, messagebox
from bigtree import Node, print_tree

# Este código es una implementación de una aplicación GUI para gestionar rutas entre ciudades utilizando un árbol.

# Esteban Francisco Janiot Rivera  cod -2191593





class Ruta:
    def __init__(self):
        self.raiz = Node("Colombia")
        self.ciudades = {}  # Diccionario para acceso rápido a las ciudades

    def agregar_ruta(self, origen, destino):
        if origen not in self.ciudades:
            self.ciudades[origen] = Node(origen, parent=self.raiz)

        if destino not in self.ciudades:
            self.ciudades[destino] = Node(destino, parent=self.ciudades[origen])
        else:
            self.ciudades[destino].parent = self.ciudades[origen]

    def existe_ruta(self, origen, destino):
        if origen not in self.ciudades or destino not in self.ciudades:
            return False

        actual = self.ciudades[destino]
        while actual:
            if actual.name == origen:
                return True
            actual = actual.parent
        return False

    def obtener_ciudades(self):
        return list(self.ciudades.keys())



#interface gráfica
class App:
    def __init__(self, root):
        self.rutas = Ruta()
        self.root = root
        self.root.title("Gestión de Rutas con Árboles")

        self.frame = tk.Frame(root, padx=10, pady=10)
        self.frame.pack()

        # Sección para agregar rutas
        tk.Label(self.frame, text="Origen:").grid(row=0, column=0, sticky="e")
        self.origen_entry = tk.Entry(self.frame)
        self.origen_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Destino:").grid(row=1, column=0, sticky="e")
        self.destino_entry = tk.Entry(self.frame)
        self.destino_entry.grid(row=1, column=1)

        self.agregar_btn = tk.Button(self.frame, text="Agregar Ruta", command=self.agregar_ruta)
        self.agregar_btn.grid(row=2, column=0, columnspan=2, pady=5)

        # Sección para consultar rutas
        tk.Label(self.frame, text="Consultar si hay ruta de").grid(row=3, column=0, columnspan=2)

        tk.Label(self.frame, text="Origen:").grid(row=4, column=0, sticky="e")
        self.origen_combo = ttk.Combobox(self.frame, state="readonly")
        self.origen_combo.grid(row=4, column=1)

        tk.Label(self.frame, text="Destino:").grid(row=5, column=0, sticky="e")
        self.destino_combo = ttk.Combobox(self.frame, state="readonly")
        self.destino_combo.grid(row=5, column=1)

        self.consultar_btn = tk.Button(self.frame, text="Consultar Ruta", command=self.consultar_ruta)
        self.consultar_btn.grid(row=6, column=0, columnspan=2, pady=5)

        # Visualizar árbol
        self.visualizar_btn = tk.Button(self.frame, text="Visualizar Árbol (Consola)", command=self.visualizar_arbol)
        self.visualizar_btn.grid(row=7, column=0, columnspan=2, pady=5)

    def agregar_ruta(self):
        origen = self.origen_entry.get().strip()
        destino = self.destino_entry.get().strip()

        if not origen or not destino:
            messagebox.showwarning("Campos vacíos", "Por favor ingresa tanto el origen como el destino.")
            return

        self.rutas.agregar_ruta(origen, destino)
        messagebox.showinfo("Ruta agregada", f"Se ha agregado la ruta de {origen} a {destino}.")

        # Limpiar campos
        self.origen_entry.delete(0, tk.END)
        self.destino_entry.delete(0, tk.END)

        # Actualizar combobox
        ciudades = self.rutas.obtener_ciudades()
        self.origen_combo['values'] = ciudades
        self.destino_combo['values'] = ciudades

    def consultar_ruta(self):
        origen = self.origen_combo.get()
        destino = self.destino_combo.get()

        if not origen or not destino:
            messagebox.showwarning("Campos vacíos", "Selecciona un origen y un destino.")
            return

        existe = self.rutas.existe_ruta(origen, destino)
        if existe:
            messagebox.showinfo("Ruta encontrada", f"Sí existe una ruta desde {origen} hasta {destino}.")
        else:
            messagebox.showinfo("Ruta no encontrada", f"No existe una ruta directa desde {origen} hasta {destino}.")

    def visualizar_arbol(self):
        print(" Estructura actual del árbol de rutas:\n")
        print_tree(self.rutas.raiz)
        print("\n(La estructura del árbol fue impresa en la consola.)")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
