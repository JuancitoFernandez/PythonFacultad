
def hash_nivel(pokemons):
    return pokemon["nivel"] % 10

def hash_tipo(pokemons):
    return tuple(pokemon["tipo"])
   
def hash_num(pokemons):
    return pokemon["numero"] % 10

tabla_nivel = {}
tabla_tipo = {}
tabla_num = {}

pokemons = [
    {"nombre": "hydreigon" ,"tipo": ["Dragon", "Siniestro"] ,"nivel": 43 ,"numero": 635},
    {"nombre": "yveltal" ,"tipo": ["Siniestro","Volador" ],"nivel": 56 ,"numero": 717},
    {"nombre": "tyrunt" ,"tipo": ["Roca", "Dragon"] ,"nivel": 2 ,"numero": 696},
    {"nombre": "vibrava" ,"tipo": ["Tierra","Dragon"] ,"nivel": 9 ,"numero": 329},
    {"nombre": "sceptile" ,"tipo": ["Planta"] ,"nivel": 71 ,"numero": 254},
    {"nombre": "scraggy" ,"tipo": ["Siniestro","Lucha"] ,"nivel": 37 ,"numero": 559},
    {"nombre": "rhyperior" ,"tipo": ["Tierra", "Roca"] ,"nivel": 69 ,"numero": 464},
    {"nombre": "rattata" ,"tipo": ["Normal"] ,"nivel": 4 ,"numero": 19},
    {"nombre": "tyranitar" ,"tipo": ["Rocar","Siniestro"] ,"nivel": 48 ,"numero": 248},
    {"nombre": "meowth" ,"tipo": ["Normal"] ,"nivel": 13 ,"numero": 52},
    {"nombre": "noivern" ,"tipo": ["Volador", "Dragon"] ,"nivel": 17 ,"numero": 715},
    {"nombre": "abra" ,"tipo": ["Psiquico"] ,"nivel": 12 ,"numero": 63},
    {"nombre": "gyarados" ,"tipo": ["Agua","Volador"] ,"nivel": 55 ,"numero": 130},
    {"nombre": "eevee" ,"tipo": ["Normal"] ,"nivel": 7 ,"numero": 133},
    {"nombre": "gengar" ,"tipo": ["Fantasma", "Veneno"] ,"nivel": 74 ,"numero": 94}
]

for pokemon in pokemons:
    # Hash por tipo
    for tipo in hash_tipo(pokemon):
        if tipo not in tabla_tipo:
            tabla_tipo[tipo] = []
        tabla_tipo[tipo].append(pokemon)
    
    # Hash por nivel
    clave_2 = hash_nivel(pokemon)
    if clave_2 not in tabla_nivel:
        tabla_nivel[clave_2] = []
    tabla_nivel[clave_2].append(pokemon)
    
    # Hash por numero
    clave_3 = hash_num(pokemon)
    if clave_3 not in tabla_num:
        tabla_num[clave_3] = []
    tabla_num[clave_3].append(pokemon)

#D. cargar un nuevo pokemon
def cargar_pokemon(nombre, tipo, nivel, numero):
    nuevo_pokemon = {"nombre": nombre, "tipo": tipo, "nivel": nivel, "numero": numero}
    pokemons.append(nuevo_pokemon)

#Mostar pokemones por el numero:
def mostrar_pokemons_por_numero(terminacion):
    for num in terminacion:
        if num in tabla_num:
            print(f"Pokémons con número terminando en {num}:")
            for pokemon in tabla_num[num]:
                print(pokemon)

#Mostar pokemones por el nivel:
def mostrar_pokemons_por_nivel(multiplos):
    for nivel in multiplos:
        if nivel in tabla_nivel:
            print(f"Pokémons con nivel múltiplo de {nivel}:")
            for pokemon in tabla_nivel[nivel]:
                print(pokemon)

#Mostrar los pokemones del siguiente tipo:
def mostrar_pokemons_por_tipo(tipos):
    for tipo in tipos:
        if tipo in tabla_tipo:
            print(f"Pokémons de tipo {tipo}:")
            for pokemon in tabla_tipo[tipo]:
                print(pokemon)

# Cargar un Pokémon nuevo de ejemplo
cargar_pokemon("charmander", ["Fuego"], 13, 4)

# Mostrar resultados
print("Pokémons cuyos números terminan en 3, 7 y 9:")
mostrar_pokemons_por_numero([3, 7, 9])

print("Pokémons cuyos niveles son múltiplos de 2, 5 y 10:")
mostrar_pokemons_por_nivel([2, 5, 10])

print("Pokémons de tipo Acero, Fuego, Eléctrico, Hielo:")
mostrar_pokemons_por_tipo(["Acero", "Fuego", "Eléctrico", "Hielo"])