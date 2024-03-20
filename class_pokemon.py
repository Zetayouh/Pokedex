
class Pokemon:
    def __init__(self, numero, nombre):
        self.numero = numero
        self.nombre = nombre
        self.habilidades = []
        self.versions = []
        self.versiones = []
        self.estadisticas = {}
        self.tipos = []

    def set_habilidad(self, habilidad):
        self.habilidades.append(habilidad)
        
    def set_exp_base(self, numero):
        self.exp_base = numero

    def set_altura(self, numero):
        self.altura = numero

    def set_versions(self, version):
        self.versions.append(version)
    
    def set_versiones(self, version):
        self.versiones.append(version)

    def set_imagen(self, imagen):
        self.imagen = imagen
    
    def set_stats(self, hp, attack, defense, special_attack, special_defense, speed):
        self.estadisticas["Vida"] = hp
        self.estadisticas["Ataque"] = attack
        self.estadisticas["Defensa"] = defense
        self.estadisticas["Ataque X"] = special_attack
        self.estadisticas["Defensa X"] = special_defense
        self.estadisticas["Velocidad"] = speed

    def set_tipo(self, url):
        self.tipos.append(url)

    def set_peso(self, peso):
        self.peso = peso

    def get_tipo(self):
        return self.tipo
    
    def get_versions(self):
        return self.versions
    
    def get_versiones(self):
        formateado = ", ".join(self.versiones)
        return formateado

    def get_imagen(self):
        return self.imagen

    def get_stats(self):
        return self.estadisticas

    def get_habilidades(self):
        return self.habilidades