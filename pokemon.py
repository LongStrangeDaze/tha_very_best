import requests as r
selected_pokemon = ["darkrai","haunter", "zacian", "gengar", "lucario"]
pokeapi = "https://pokeapi.co/api/v2/pokemon/"

for pokemon in selected_pokemon:
    result = r.get(f"{pokeapi}{pokemon}")
    pokedata = result.json()

    print(f'{pokedata["name"]}({pokedata["id"]}) - Base XP {pokedata["base_experience"]} - {pokedata["sprites"]["front_shiny"]} - {pokedata["abilities"][0]["ability"]["name"]}')