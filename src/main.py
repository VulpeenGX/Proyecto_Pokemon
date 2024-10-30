# %%Imports
import json
import os
import random
# %% Rutas
# Obtener la ruta absoluta del directorio donde se está ejecutando el programa
current_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..')) # '..' nos lleva a un directorio superior del que estamos 
file_path = os.path.join(project_dir, 'data', 'pokemons1.json')
types_path = os.path.join(project_dir, 'data', 'tipos.json')
abilities_path = os.path.join(project_dir, 'data', 'abilities.json')

# %%Datas
# Cargar datos de Pokémon desde un archivo JSON
def load_files(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

# Mostrar la lista de Pokémon disponibles
def show_pokemons(pokemons):
    for pokemon in pokemons:
        print(f"{pokemon['id']}: {pokemon['name']} (HP: {pokemon['hp']}, Attack: {pokemon['attack']}, Defense: {pokemon['defense']}, Special Attack: {pokemon['special_attack']}, Special Defense: {pokemon['special_defense']}, Speed: {pokemon['speed']}, Type: {', '.join(pokemon['type'])})")



# %% Metodos
def choose_pokemon(pokemons):
    while True:
        try:
            choice = int(input("Elige el ID del Pokémon: "))
            if 1 <= choice <= 151:
                return pokemons[choice - 1]
            else:
                print("ID inválido. Por favor, elige un ID de la lista.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

def types(attacker_types, defender_types, types_data):
    multiplier = 1.0
    for attacker_type in attacker_types:
        for defender_type in defender_types:
            if defender_type in types_data[attacker_type]['strong_against']:
                multiplier *= 2.0
            elif defender_type in types_data[attacker_type]['weak_against']:
                multiplier *= 1.5
            elif defender_type in types_data[attacker_type]['immune_against']:
                multiplier *= 1
    return multiplier

def battle(pokemon1, pokemon2, abilities, types_data):
    print(f"\n¡{pokemon1['name']} vs {pokemon2['name']}!\n")
    print(f"Tipos de {pokemon1['name']}: {', '.join(pokemon1['type'])}")
    print(f"Tipos de {pokemon2['name']}: {', '.join(pokemon2['type'])}\n")
    
    for _ in range(3):  
        random_ability1 = random.choice(abilities["abilities"])
        random_ability2 = random.choice(abilities["abilities"])
        
        print(f"{pokemon1['name']} utiliza {random_ability1['name']} - {random_ability1['description']}")
        print(f"{pokemon2['name']} utiliza {random_ability2['name']} - {random_ability2['description']}\n")

    multiplier1 = types(pokemon1['type'], pokemon2['type'], types_data)
    multiplier2 = types(pokemon2['type'], pokemon1['type'], types_data)
    damage1 = (pokemon1['attack'] + pokemon1['special_attack'] + pokemon1['speed']) * multiplier1
    damage2 = (pokemon2['attack'] + pokemon2['special_attack'] + pokemon2['speed']) * multiplier2
    defence1 = pokemon1['defense'] + pokemon1['special_defense']
    defence2 = pokemon2['defense'] + pokemon2['special_defense']
    stats1 = pokemon1['hp'] + defence1 - damage2 + random.randint(-100, 200)
    stats2 = pokemon2['hp'] + defence2 - damage1 + random.randint(-100, 200)

    if stats1 > stats2:
        print(f"El ganador es: {pokemon1['name']}")
    elif stats2 > stats1:
        print(f"El ganador es: {pokemon2['name']}")
    else:
        print("¡Es un empate!")


# Menu
def menu():
    pokemons = load_files(file_path)
    types_data = load_files(types_path)
    abilities = load_files(abilities_path)
    show_pokemons(pokemons)
    print("Elige un Pokémon")
    pokemon1 = choose_pokemon(pokemons)
    print("Elige otro Pokémon")
    pokemon2 = choose_pokemon(pokemons)
    battle(pokemon1, pokemon2, abilities, types_data)

menu()
