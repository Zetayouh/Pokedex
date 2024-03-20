from tkinter import Toplevel

from colocacion import *

def abrir_ventana_habilidad(self, numero_habilidad):
    #Creación de ventana de Ayuda
    ventana_habilidad = Toplevel()
    ventana_habilidad.title("Información de habilidad")
    ventana_habilidad.config(background="black", width=800, height=530)
    
    #Fila 0
    titulo_nombre = colocar_label_info(ventana_habilidad, "Nombre: ")
    titulo_nombre.grid(row=0, column=0, padx=10, pady=10)
    titulo_nombre.config(background="black", fg="red")
    info_nombre = colocar_label_info(ventana_habilidad, self.habilidades.nombre[numero_habilidad])
    info_nombre.grid(row=0, column=1, padx=10, pady=10)
    info_nombre.config(background="black", fg="red")
    #Fila 1
    titulo_efecto = colocar_label_info(ventana_habilidad, "Efecto: ")
    titulo_efecto.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    titulo_efecto.config(background="black", fg="yellow", justify="center")
    info_efecto = colocar_label_info(ventana_habilidad, self.habilidades.efecto[numero_habilidad])
    info_efecto.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    info_efecto.config(background="black", fg="white", justify="center")
    

    
