from tkinter import Toplevel

from colocacion import *

def abrir_ventana_tipo(mi_tipo):
    #Creación de ventana de Ayuda
    ventana_tipo = Toplevel()
    ventana_tipo.title("Información de daños".format(mi_tipo.nombre))
    ventana_tipo.config(background="black", width=800, height=530)
    
    #Fila 0
    titulo_info_daños = colocar_label_info(ventana_tipo, "Información de tipo {}".format(mi_tipo.nombre), fuente=("Arial", 40))
    titulo_info_daños.grid(row=0, column=0, columnspan=6)
    titulo_info_daños.config(background="black", fg="purple", justify="center", pady=10)
    #Fila 1
    titulo_doble_daño_de = colocar_label_info(ventana_tipo, "Recibe doble daño de: ")
    info_doble_daño_de = colocar_label_info(ventana_tipo, mi_tipo.get_doble_daño_de())
    #Fila 2
    titulo_doble_daño_a = colocar_label_info(ventana_tipo, "Hace doble daño a: ")
    info_doble_daño_a = colocar_label_info(ventana_tipo, mi_tipo.get_doble_daño_a())
    #Fila3
    titulo_medio_daño_de = colocar_label_info(ventana_tipo, "Recibe la mitad de daño de: ")
    info_medio_daño_de = colocar_label_info(ventana_tipo, mi_tipo.get_medio_daño_de())
    #Fila4
    titulo_medio_daño_a = colocar_label_info(ventana_tipo, "Hace la mitad de daño a: ")
    info_medio_daño_a = colocar_label_info(ventana_tipo, mi_tipo.get_medio_daño_a())
    #Fila5
    titulo_no_daño_de = colocar_label_info(ventana_tipo, "No recibe daño de: ")
    info_no_daño_de = colocar_label_info(ventana_tipo, mi_tipo.get_no_daño_de())
    #Fila6
    titulo_no_daño_a = colocar_label_info(ventana_tipo, "No hace daño a: ")
    info_no_daño_a = colocar_label_info(ventana_tipo, mi_tipo.get_no_daño_a())

    lista_labels = [titulo_doble_daño_de, info_doble_daño_de, 
                    titulo_doble_daño_a, info_doble_daño_a, 
                    titulo_medio_daño_de, info_medio_daño_de, 
                    titulo_medio_daño_a, info_medio_daño_a, 
                    titulo_no_daño_de, info_no_daño_de, 
                    titulo_no_daño_a, info_no_daño_a]
    
    organizar_ventana(lista_labels, 6, 2)

