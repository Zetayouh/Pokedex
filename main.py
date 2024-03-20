from tkinter import Tk

from colocacion import *
from consulta import *
from ventana_informacion import *

root=Tk()

class Pokedex:
    def __init__(self, root):
        #Parametros del root
        self.root = root
        self.root.title("Pokedex")
        self.root.config(background="black") #agregar aqui barra_menu
     
        #Variables generales
        self.texto_nombre_numero = StringVar()
        self.texto_tipo1 = StringVar()
        self.texto_tipo2 = StringVar()
        self.texto_version = StringVar()
        self.texto_movimiento = StringVar()

        self.lista_textos = [self.texto_nombre_numero, self.texto_tipo1, self.texto_tipo2, self.texto_version, self.texto_movimiento]
     
        #Fila 1
        self.label_nombre_numero = colocar_label(self, "Nombre o Nº de Pokemon")
        self.label_nombre_numero.grid(row=0, column=0, padx=10, sticky="w")
        self.label_nombre_numero.config(background="black", fg="white")
        self.entry_nombre_numero = Entry(self.root, textvariable=self.texto_nombre_numero, justify="right")
        self.entry_nombre_numero.grid(row=0, column=1, padx=10, sticky="e")

        #Boton buscar
        self.boton_buscar = Button(self.root, text="Buscar", font=("Arial", 18))
        self.boton_buscar.grid(row=6, column=0, columnspan=2)
        self.boton_buscar.config(background="grey", activebackground="grey", pady=10, command=lambda: self.set_pokemon(self.texto_nombre_numero.get()))

    def set_pokemon(self, numero_nombre):
        self.pokemon, self.habilidades = consulta_pokemon(numero_nombre)
        abrir_ventana_informacion(self)

if __name__ == '__main__':
    mi_pokedex = Pokedex(root)
    root.mainloop()