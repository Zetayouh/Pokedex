from tkinter import Toplevel

from colocacion import *
from consulta_tipos import *
from class_tipo import *
from ventana_informacion import *
from ventana_habilidad import *

def abrir_ventana_informacion(self):
    #Creación de ventana de Ayuda
    ventana_informacion = Toplevel()
    ventana_informacion.title("Información de Pokemon")
    ventana_informacion.config(background="black", width=800, height=530)
    
    #Labels de ayuda
    #Fila 0
    titulo_info_gen = colocar_label_info(ventana_informacion, "Información general:", fuente=("Arial", 40))
    titulo_info_gen.grid(row=0, column=0, columnspan=6)
    titulo_info_gen.config(background="black", fg="blue", justify="center", pady=10)
    #Fila 1
    titulo_imagen = colocar_label_info(ventana_informacion, "Imagen: ")
    info_imagen = Label(ventana_informacion, image=self.pokemon.get_imagen())
    titulo_id = colocar_label_info(ventana_informacion, "Pokemon ID: ")
    info_id = colocar_label_info(ventana_informacion, self.pokemon.numero)
    titulo_nombre = colocar_label_info(ventana_informacion, "Nombre: ")
    info_nombre = colocar_label_info(ventana_informacion, self.pokemon.nombre)
    #Fila 2
    titulo_exp = colocar_label_info(ventana_informacion, "Exp base: ")
    info_exp = colocar_label_info(ventana_informacion, self.pokemon.exp_base)
    titulo_altura = colocar_label_info(ventana_informacion, "Altura: ")
    info_altura = colocar_label_info(ventana_informacion, self.pokemon.altura)
    titulo_peso = colocar_label_info(ventana_informacion, "Peso: ")
    info_peso = colocar_label_info(ventana_informacion, self.pokemon.peso)
    #Fila 3
    titulo_estadisticas = colocar_label_info(ventana_informacion, "Estadisticas:", fuente=("Arial", 40))
    titulo_estadisticas.grid(row=3, column=0, columnspan=6)
    titulo_estadisticas.config(background="black", fg="red", justify="center", pady=20)
    #Fila 4
    titulo_vida =  colocar_label_info(ventana_informacion, "Vida: ")
    info_vida = colocar_label_info(ventana_informacion, self.pokemon.estadisticas["Vida"])
    titulo_ataque =  colocar_label_info(ventana_informacion, "Ataque: ")
    info_ataque = colocar_label_info(ventana_informacion, self.pokemon.estadisticas["Ataque"])
    titulo_defensa =  colocar_label_info(ventana_informacion, "Defensa: ")
    info_defensa = colocar_label_info(ventana_informacion, self.pokemon.estadisticas["Defensa"])
    #Fila 5
    titulo_ataque_x =  colocar_label_info(ventana_informacion, "Ataque X: ")
    info_ataque_x = colocar_label_info(ventana_informacion, self.pokemon.estadisticas["Ataque X"])
    titulo_defensa_x =  colocar_label_info(ventana_informacion, "Defensa X: ")
    info_defensa_x = colocar_label_info(ventana_informacion, self.pokemon.estadisticas["Defensa X"])
    titulo_velocidad =  colocar_label_info(ventana_informacion, "Velocidad: ")
    info_velocidad = colocar_label_info(ventana_informacion, self.pokemon.estadisticas["Velocidad"])
    #Fila 6
    titulo_tipo = colocar_label_info(ventana_informacion, "Tipo:", fuente=("Arial", 40))
    titulo_tipo.grid(row=6, column=0, columnspan=6)
    titulo_tipo.config(background="black", fg="brown", justify="center", pady=20)
    #Fila 7
    boton1 = Button
    boton2 = Button
    boton3 = Button
    botones = [boton1, boton2, boton3]
    tipos = []
    cont=0                   
        
    for url_tipo in self.pokemon.tipos:
        tipos.append(crea_tipo(url_tipo))
        botones[cont] = coloca_boton(ventana_informacion, tipos[cont].nombre)
        botones[cont].grid(row=7, column=cont*2, columnspan=2)
        cont+=1
    
    botones[0].config(background="grey", activebackground="grey", pady=10, command=lambda: abrir_ventana_tipo(tipos[0]))
    if len(tipos) >= 2:
        botones[1].config(background="grey", activebackground="grey", pady=10, command=lambda: abrir_ventana_tipo(tipos[1]))
    if len(tipos) >= 3:
        botones[2].config(background="grey", activebackground="grey", pady=10, command=lambda: abrir_ventana_tipo(tipos[2])) 
        
    #Fila 8
    titulo_habilidades = colocar_label_info(ventana_informacion, "Habilidades: ", fuente=("Arial", 40))
    titulo_habilidades.grid(row=8, column=0, columnspan=6)
    titulo_habilidades.config(background="black", fg="orange", justify="center", pady=20)
    #Fila 9
    boton_1 = Button
    boton_2 = Button
    boton_3 = Button
    botones_habilidad = [boton_1, boton_2, boton_3]
    habilidades = 0
    for i, clave in enumerate(self.habilidades.nombre):
        habilidades += 1
        botones_habilidad[i] = coloca_boton(ventana_informacion, self.habilidades.nombre[clave])
        botones_habilidad[i].grid(row=9, column=i*2, columnspan=2)
    
    botones_habilidad[0].config(background="grey", activebackground="grey", pady=10, command=lambda: abrir_ventana_habilidad(self, self.pokemon.habilidades[0]))
    if habilidades >= 2:
        botones_habilidad[1].config(background="grey", activebackground="grey", pady=10, command=lambda: abrir_ventana_habilidad(self, self.pokemon.habilidades[1]))
    if habilidades >= 3:
        botones_habilidad[2].config(background="grey", activebackground="grey", pady=10, command=lambda: abrir_ventana_habilidad(self, self.pokemon.habilidades[2]))   
    #Fila 10
    titulo_versiones = colocar_label_info(ventana_informacion, "Versiones: ", fuente=("Arial", 40))
    titulo_versiones.grid(row=10, column=0, columnspan=6)
    titulo_versiones.config(background="black", fg="green", justify="center", pady=20)
    #Fila 11
    info_versiones = colocar_label_info(ventana_informacion, self.pokemon.get_versiones())
    info_versiones.grid(row=11, column=0, columnspan=6, sticky="w")
    info_versiones.config(background="black", fg="white", justify="left", pady=10, padx=10)

    #Lista de labels
    lista_labels = [titulo_imagen, info_imagen, titulo_id, info_id, titulo_nombre, info_nombre, 
                    titulo_exp, info_exp, titulo_altura, info_altura, titulo_peso, info_peso,  
                    titulo_vida, info_vida, titulo_ataque, info_ataque, titulo_defensa, info_defensa, 
                    titulo_ataque_x, info_ataque_x, titulo_defensa_x, info_defensa_x, titulo_velocidad, info_velocidad, 
                    ]
    
    #Llamada a la funcion de organizar la ventana
    organizar_ventana_informacion(lista_labels, 4, 6)