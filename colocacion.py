from tkinter import *

#Creación de labels
def colocar_label(self, texto, fuente=("Arial", 30)):
    return Label(self.root, text=texto, font=fuente)

def colocar_label_info(ventana, texto, fuente=("Arial", 30)):
    return Label(ventana, text=texto, font=fuente, wraplength=1200)

def coloca_boton(ventana, texto):
    return Button(ventana, text=texto, font=("Arial", 30))

#Colocación de todos los labels y checkbutons en el grid
def organizar_pantalla(self, filas, columnas):
    contador = 0
    for fila in range(filas):
        for columna in range(columnas):          
            if columna == 0:
                self.labels[contador].grid(row=fila, column=columna, padx=10, sticky="w")
                self.labels[contador].config(background="black", fg="white")
            else:
                self.labels[contador].grid(row=fila, column=columna, padx=10, sticky="e")
            
            contador+=1

def organizar_ventana_informacion(labels, filas, columnas):
    contador = 0
    for fila in range(filas):
        for columna in range(columnas):
            if fila >= 2:
                labels[contador].grid(row=fila+2, column=columna, padx=10, sticky="w")
            else:
                labels[contador].grid(row=fila+1, column=columna, padx=10, sticky="w")

            if columna % 2 == 0:
                labels[contador].config(background="black", fg="yellow", justify="left")
            else:               
                labels[contador].config(background="black", fg="white", justify="left")
            contador+=1

def organizar_ventana(labels, filas, columnas):
    contador = 0
    for fila in range(filas):
        for columna in range(columnas):      
            labels[contador].grid(row=fila+1, column=columna, padx=10, sticky="w")
            if columna == 0:
                labels[contador].config(background="black", fg="green")
            else:
                labels[contador].config(background="black", fg="white")
            contador+=1