import requests
from PIL import Image
from io import BytesIO
from googletrans import Translator

from class_pokemon import Pokemon
from consulta_habilidad import *
from class_habilidades import Habilidades
from trabajo_de_imagenes import redimensiona

def consulta_pokemon(numero_nombre, url="https://pokeapi.co/api/v2/pokemon/"):
    response = requests.get(url+numero_nombre)
    if response.status_code == 200:

        payload = response.json()
        forms = payload.get("forms", [])

        nombre = forms[0]["name"]
        id = payload.get("id")
        mi_pokemon = Pokemon(id, nombre)
        mis_habilidades = Habilidades()

        habilidades = payload.get("abilities", [])
        for habilidad in habilidades:
            url_habilidad = habilidad["ability"].get("url", [])
            splited_url = url_habilidad.split("/")
            numero_habilidad = splited_url[-2]
            mi_pokemon.set_habilidad(numero_habilidad)
            consulta_habilidad(url_habilidad, numero_habilidad, mis_habilidades)

        base_experience = payload.get("base_experience", [])
        mi_pokemon.set_exp_base(base_experience)

        altura = payload.get("height", [])
        mi_pokemon.set_altura(altura)

        game_indices = payload.get("game_indices", [])
        for version in game_indices:
            mi_pokemon.set_versions(version["version"]["name"])

        if mi_pokemon.get_versions() != []:
            text = mi_pokemon.get_versions()
            separador = ", "
            text = separador.join(text)
            
            translator = Translator()
            translation = translator.translate(text, src='en', dest='es')
            mi_pokemon.set_versiones(translation.text)

        sprites = payload.get("sprites", [])
        url_imagen = sprites["front_default"]
        respuesta = requests.get(url_imagen)
        img = Image.open(BytesIO(respuesta.content))
        photo = redimensiona((140, 140), img)
        mi_pokemon.set_imagen(photo)

        stats = payload.get("stats", [])
        mi_pokemon.set_stats(stats[0]["base_stat"], stats[1]["base_stat"], stats[2]["base_stat"], stats[3]["base_stat"], stats[4]["base_stat"], stats[5]["base_stat"])

        weight = payload.get("weight", [])
        mi_pokemon.set_peso(weight)

        tipos = payload.get("types", [])
        for i in tipos:
            url_tipo = i["type"]["url"]
            mi_pokemon.set_tipo(url_tipo)
        
        return mi_pokemon, mis_habilidades
  