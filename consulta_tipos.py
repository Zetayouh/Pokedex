import requests

from colocacion import *
from class_tipo import *
from ventana_tipo import *

diccionario_tipo = {"normal":"normal", "fighting":"luchador", "flying":"volador", "poison":"veneno", 
                    "ground":"tierra", "rock":"roca", "bug":"bicho", "ghost":"fantasma", "steel":"acero", 
                    "fire":"fuego", "water":"agua", "grass":"hierba", "electric":"electrico", 
                    "psychic":"psiquico", "ice":"hielo", "dragon":"dragon", "dark":"oscuridad", 
                    "fairy":"hada"}

def traduce(palabra):
    if palabra in diccionario_tipo:
        return diccionario_tipo[palabra]

def crea_tipo(url_tipo):
   
    response = requests.get(url_tipo)
    if response.status_code == 200:
        payload = response.json()
        names = payload.get("names")
        for i in names:
            if i["language"]["name"] == "es":
                nombre_tipo = i["name"]
       
        mi_tipo = Tipo(nombre_tipo)
        relacion_daños = payload.get("damage_relations")
        for i in relacion_daños["double_damage_from"]:
            nombre = traduce(i["name"])
            mi_tipo.set_doble_daño_de(nombre)
        for i in relacion_daños["double_damage_to"]:
            nombre = traduce(i["name"])
            mi_tipo.set_doble_daño_a(nombre)
        for i in relacion_daños["half_damage_from"]:
            nombre = traduce(i["name"])
            mi_tipo.set_medio_daño_de(nombre)
        for i in relacion_daños["half_damage_to"]:
            nombre = traduce(i["name"])
            mi_tipo.set_medio_daño_a(nombre)
        for i in relacion_daños["no_damage_from"]:
            nombre = traduce(i["name"])
            mi_tipo.set_no_daño_de(nombre)
        for i in relacion_daños["no_damage_to"]:
            nombre = traduce(i["name"])
            mi_tipo.set_no_daño_a(nombre)

        return mi_tipo
    

