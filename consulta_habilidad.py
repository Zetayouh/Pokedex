import requests
from googletrans import Translator

def consulta_habilidad(url, numero_habilidad, mis_habilidades):
    response = requests.get(url)
    if response.status_code == 200:

        payload = response.json()
        names = payload.get("names")
        for index in names:
            if index["language"]["name"] == "es":
                nombre_habilidad = index["name"]
                mis_habilidades.set_nombre(numero_habilidad, nombre_habilidad)

        effect_entries = payload.get("effect_entries")
        for i, entry in enumerate(effect_entries):
            if entry["language"]["name"] == "en":
                text = effect_entries[i]["effect"]
                translator = Translator()
                translation = translator.translate(text, src='en', dest='es')
                efecto = translation.text.replace(";", ". ")
                mis_habilidades.set_efecto(numero_habilidad, efecto)

