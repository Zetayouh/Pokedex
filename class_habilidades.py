
class Habilidades:
    def __init__(self):
        self.nombre = {}
        self.efecto = {}

    def set_nombre(self, numero, nombre):
        self.nombre[numero] = nombre

    def set_efecto(self, numero, efecto):
        self.efecto[numero] = efecto