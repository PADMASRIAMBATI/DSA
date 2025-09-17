# How to connect to an API using Python

import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        print(f"Data is Retrieved!")
        return pokemon_data
    else:
        print(f"Failed to Retrieved Data! {response.status_code}")
        return None

pokemon_info = get_pokemon_info("pikachu")

if pokemon_info:
    print(f"Name: {pokemon_info["name"]}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")
else:
    print("Not Found")