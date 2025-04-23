# Primer entrega del proyecto de rutas
# Esteban Francisco Janiot Rivera -2191593
# Santiago Andres Moreno Garcia -2221879
# Harold Peña -2232733
# Juan David Alfonso -2232878

import tkinter as tk
from tkinter import ttk, messagebox

# ---------- CLASES PARA LA LISTA CIRCULAR DOBLEMENTE ENLAZADA ----------
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazadaDC:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0
    
    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            ultimo = self.cabeza.anterior
            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = ultimo
            self.cabeza.anterior = nuevo_nodo
            ultimo.siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamano += 1
    
    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.insertar_al_inicio(dato)
        else:
            ultimo = self.cabeza.anterior
            ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = ultimo
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.tamano += 1
    
    def insertar_en_posicion(self, dato, posicion):
        if posicion < 0 or posicion > self.tamano:
            raise ValueError("Posición inválida")
        if posicion == 0:
            self.insertar_al_inicio(dato)
        elif posicion == self.tamano:
            self.insertar_al_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion - 1):
                actual = actual.siguiente
            siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            nuevo_nodo.siguiente = siguiente
            siguiente.anterior = nuevo_nodo
            self.tamano += 1
    
    def buscar(self, dato):
        if not self.cabeza:
            return None
        actual = self.cabeza
        for _ in range(self.tamano):
            if actual.dato == dato:
                return actual
            actual = actual.siguiente
        return None
    
    def mostrar(self):
        elementos = []
        actual = self.cabeza
        for _ in range(self.tamano):
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

# ---------- FUNCIONES DE CÁLCULO DE PASOS ----------
def calcular_pasos_entre_nodos(lista, nodo_a, nodo_b):
    # Calcula pasos mínimos entre dos nodos (adelante o atrás)
    pasos_adelante = 0
    actual = nodo_a
    while actual != nodo_b:
        actual = actual.siguiente
        pasos_adelante += 1
        if actual == nodo_a:  # Evitar bucle infinito
            return -1
    
    pasos_atras = 0
    actual = nodo_a
    while actual != nodo_b:
        actual = actual.anterior
        pasos_atras += 1
        if actual == nodo_a:
            return -1
    
    return min(pasos_adelante, pasos_atras)

def calcular_ruta_completa(lista, puntos):
    total_pasos = 0
    for i in range(len(puntos) - 1):
        nodo_actual = lista.buscar(puntos[i])
        nodo_siguiente = lista.buscar(puntos[i + 1])
        if not nodo_actual or not nodo_siguiente:
            return -1  # Error: nodo no existe
        pasos = calcular_pasos_entre_nodos(lista, nodo_actual, nodo_siguiente)
        if pasos == -1:
            return -1
        total_pasos += pasos
    return total_pasos

# ---------- INTERFAZ GRÁFICA ----------
class InterfazDomiciliario:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Rutas ")
        self.lista = ListaEnlazadaDC()
        
        # Frame para inserción de nodos
        self.frame_insercion = ttk.Frame(root)
        self.label_nuevo_punto = ttk.Label(self.frame_insercion, text="Nuevo punto:")
        self.entry_nuevo_punto = ttk.Entry(self.frame_insercion, width=10)
        self.label_posicion = ttk.Label(self.frame_insercion, text="Posición:")
        self.combo_posicion = ttk.Combobox(self.frame_insercion, values=["Inicio", "Final", "Posición"], width=10)
        self.entry_posicion = ttk.Entry(self.frame_insercion, width=5)
        self.btn_agregar = ttk.Button(self.frame_insercion, text="Agregar", command=self.agregar_punto)
        
        # Frame para creación de rutas
        self.frame_ruta = ttk.Frame(root)
        self.combo_puntos = ttk.Combobox(self.frame_ruta, width=10)
        self.btn_agregar_ruta = ttk.Button(self.frame_ruta, text="Agregar a Ruta", command=self.agregar_a_ruta)
        self.listbox_ruta = tk.Listbox(self.frame_ruta, width=30, height=5)
        self.btn_calcular = ttk.Button(self.frame_ruta, text="Calcular Pasos", command=self.calcular_pasos)
        self.label_resultado = ttk.Label(self.frame_ruta, text="")
        
        # Listbox para mostrar la lista completa
        self.listbox_lista = tk.Listbox(root, width=30, height=10)
        
        # Ubicar componentes
        self.frame_insercion.pack(padx=10, pady=10)
        self.label_nuevo_punto.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nuevo_punto.grid(row=0, column=1, padx=5, pady=5)
        self.label_posicion.grid(row=0, column=2, padx=5, pady=5)
        self.combo_posicion.grid(row=0, column=3, padx=5, pady=5)
        self.entry_posicion.grid(row=0, column=4, padx=5, pady=5)
        self.btn_agregar.grid(row=0, column=5, padx=5, pady=5)
        
        self.frame_ruta.pack(padx=10, pady=10)
        self.combo_puntos.grid(row=0, column=0, padx=5, pady=5)
        self.btn_agregar_ruta.grid(row=0, column=1, padx=5, pady=5)
        self.listbox_ruta.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.btn_calcular.grid(row=2, column=0, columnspan=2, pady=5)
        self.label_resultado.grid(row=3, column=0, columnspan=2)
        
        self.listbox_lista.pack(padx=10, pady=10)
        
        # Configurar eventos
        self.combo_posicion.bind("<<ComboboxSelected>>", self.actualizar_visibilidad_posicion)
        self.actualizar_combobox_puntos()
        self.actualizar_listbox()
    
    def actualizar_visibilidad_posicion(self, event):
        if self.combo_posicion.get() == "Posición":
            self.entry_posicion.config(state="normal")
        else:
            self.entry_posicion.config(state="disabled")
    
    def agregar_punto(self):
        dato = self.entry_nuevo_punto.get()
        if not dato:
            messagebox.showerror("Error", "Ingrese un nombre para el punto.")
            return
        
        posicion_tipo = self.combo_posicion.get()
        try:
            if posicion_tipo == "Inicio":
                self.lista.insertar_al_inicio(dato)
            elif posicion_tipo == "Final":
                self.lista.insertar_al_final(dato)
            elif posicion_tipo == "Posición":
                posicion = int(self.entry_posicion.get())
                self.lista.insertar_en_posicion(dato, posicion)
            else:
                messagebox.showerror("Error", "Seleccione un tipo de posición válido.")
                return
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        
        self.actualizar_listbox()
        self.actualizar_combobox_puntos()
        self.entry_nuevo_punto.delete(0, tk.END)
        self.entry_posicion.delete(0, tk.END)
    
    def agregar_a_ruta(self):
        punto = self.combo_puntos.get()
        if punto:
            self.listbox_ruta.insert(tk.END, punto)
    
    def calcular_pasos(self):
        puntos = self.listbox_ruta.get(0, tk.END)
        if len(puntos) < 2:
            messagebox.showerror("Error", "La ruta debe tener al menos 2 puntos.")
            return
        
        total_pasos = calcular_ruta_completa(self.lista, puntos)
        if total_pasos == -1:
            self.label_resultado.config(text="Error: Uno o más nodos no existen.")
        else:
            self.label_resultado.config(text=f"Ruta: {' → '.join(puntos)}\nTotal de pasos: {total_pasos}")
    
    def actualizar_listbox(self):
        self.listbox_lista.delete(0, tk.END)
        for elemento in self.lista.mostrar():
            self.listbox_lista.insert(tk.END, elemento)
    
    def actualizar_combobox_puntos(self):
        self.combo_puntos['values'] = self.lista.mostrar()

# ---------- EJECUCIÓN ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazDomiciliario(root)
    root.mainloop()