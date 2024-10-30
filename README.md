Pokémon Battle Simulator
Este proyecto es un simulador de batallas Pokémon que permite a los usuarios elegir y enfrentar diferentes Pokémon en una batalla simulada. Utiliza archivos JSON para cargar datos de Pokémon, tipos y habilidades.

Requisitos
Python 3.7 o superior

Bibliotecas:

json

os

random

Archivos del Proyecto
main.py: Contiene el código principal del programa.

data/pokemons1.json: Archivo JSON que contiene datos de los Pokémon.

data/tipos.json: Archivo JSON que contiene los tipos de Pokémon y sus relaciones de efectividad.

data/abilities.json: Archivo JSON que contiene las habilidades de los Pokémon.

Estructura del Proyecto

Copiar
PokemonBattleSimulator/
├── data/
│   ├── pokemons1.json
│   ├── tipos.json
│   └── abilities.json
├── main.py
└── README.md
Instrucciones de Uso
Clonar el repositorio:

sh

Copiar
git clone https://github.com/tuusuario/PokemonBattleSimulator.git
cd PokemonBattleSimulator
Ejecutar el programa:

sh

Copiar
python main.py
Descripción del Código
main.py
Imports: Importa las bibliotecas necesarias (json, os, random).

Rutas: Define las rutas de los archivos JSON.

python

Copiar
current_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..'))
file_path = os.path.join(project_dir, 'data', 'pokemons1.json')
types_path = os.path.join(project_dir, 'data', 'tipos.json')
abilities_path = os.path.join(project_dir, 'data', 'abilities.json')
Funciones:

load_files(file_name): Carga datos desde un archivo JSON.

show_pokemons(pokemons): Muestra la lista de Pokémon disponibles.

choose_pokemon(pokemons): Permite al usuario elegir un Pokémon por su ID.

types(attacker_types, defender_types, types_data): Calcula el multiplicador de daño basado en los tipos de los Pokémon.

battle(pokemon1, pokemon2, abilities, types_data): Simula una batalla entre dos Pokémon.

menu(): Menú principal que inicia el proceso de selección y batalla de Pokémon.

Archivos JSON
pokemons1.json: Contiene una lista de Pokémon con sus atributos.

json

Copiar
[
    {
        "id": 1,
        "name": "Bulbasaur",
        "hp": 45,
        "attack": 49,
        ...
    },
    ...
]
tipos.json: Define las relaciones de efectividad entre tipos de Pokémon.

json

Copiar
{
    "Grass": {
        "strong_against": ["Water", "Ground", "Rock"],
        "weak_against": ["Fire", "Ice", "Poison"],
        "immune_against": []
    },
    ...
}
abilities.json: Lista de habilidades que los Pokémon pueden usar.

json

Copiar
{
    "abilities": [
        {
            "name": "Overgrow",
            "description": "Boosts the power of Grass-type moves."
        },
        ...
    ]
}
Contribuciones
Las contribuciones son bienvenidas. Por favor, crea un 'pull request' o abre un 'issue' para discutir cualquier cambio que te gustaría realizar.

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
