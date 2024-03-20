class Tipo:
    def __init__(self, nombre_tipo):
        self.nombre = nombre_tipo
        self.doble_daño_de = []
        self.doble_daño_a = []
        self.medio_daño_de = []
        self.medio_daño_a = []
        self.no_daño_de = []
        self.no_daño_a = []

    def set_doble_daño_de(self, nombre):
        self.doble_daño_de.append(nombre)

    def set_doble_daño_a(self, nombre):
        self.doble_daño_a.append(nombre)

    def set_medio_daño_de(self, nombre):
        self.medio_daño_de.append(nombre)
    
    def set_medio_daño_a(self, nombre):
        self.medio_daño_a.append(nombre)
    
    def set_no_daño_de(self, nombre):
        self.no_daño_de.append(nombre)

    def set_no_daño_a(self, nombre):
        self.no_daño_a.append(nombre)

    def get_doble_daño_de(self):
        formateado = ", ".join(self.doble_daño_de)
        return formateado

    def get_doble_daño_a(self):
        formateado = ", ".join(self.doble_daño_a)
        return formateado

    def get_medio_daño_de(self):
        formateado = ", ".join(self.medio_daño_de)
        return formateado
    
    def get_medio_daño_a(self):
        formateado = ", ".join(self.medio_daño_a)
        return formateado
    
    def get_no_daño_de(self):
        formateado = ", ".join(self.no_daño_de)
        return formateado
    
    def get_no_daño_a(self):
        formateado = ", ".join(self.no_daño_a)
        return formateado
    
    