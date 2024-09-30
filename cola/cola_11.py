from cola import Queque

# Lista de personajes
personajes = [
    {'nombre': 'Leia Organa', 'altura': 150, 'edad': 22, 'género': 'femenino', 'especie': 'Humano', 'planeta_natal': 'Alderaan', 'episodios': [4, 5, 6, 7]},
    {'nombre': 'Darth Vader', 'altura': 202, 'edad': 45, 'género': 'masculino', 'especie': 'Humano', 'planeta_natal': 'Tatooine', 'episodios': [4, 5, 6]},
    {'nombre': 'Han Solo', 'altura': 180, 'edad': 33, 'género': 'masculino', 'especie': 'Humano', 'planeta_natal': 'Corellia', 'episodios': [4, 5, 6, 7]},
    {'nombre': 'C-3PO', 'altura': 167, 'edad': 112, 'género': 'masculino', 'especie': 'Droide', 'planeta_natal': 'Tatooine', 'episodios': [1, 2, 3, 4, 5, 6]},
    {'nombre': 'R2-D2', 'altura': 96, 'edad': 112, 'género': 'masculino', 'especie': 'Droide', 'planeta_natal': 'Naboo', 'episodios': [1, 2, 3, 4, 5, 6, 7]},
    {'nombre': 'Yoda', 'altura': 66, 'edad': 900, 'género': 'masculino', 'especie': 'Desconocido', 'planeta_natal': 'Desconocido', 'episodios': [1, 2, 3, 5, 6]},
    {'nombre': 'Chewbacca', 'altura': 228, 'edad': 200, 'género': 'masculino', 'especie': 'Wookiee', 'planeta_natal': 'Kashyyyk', 'episodios': [3, 4, 5, 6, 7]}
]

# a. Listar todos los personajes de género femenino
cola = Queque()
for p in personajes:
    cola.arrive(p)

print("\n--- a. Personajes de género femenino ---")
while cola.size() > 0:
    personaje = cola.attention()
    if personaje['género'] == 'femenino':
        print(f"Nombre: {personaje['nombre']}, Edad: {personaje['edad']}, Planeta Natal: {personaje['planeta_natal']}, Episodios: {personaje['episodios']}")

# b. Listar todos los personajes de especie Droide que aparecieron en los primeros seis episodios
cola = Queque()
for p in personajes:
    cola.arrive(p)

print("\n--- b. Droides que aparecieron en episodios 1 al 6 ---")
while cola.size() > 0:
    personaje = cola.attention()
    if personaje['especie'] == 'Droide' and any(e <= 6 for e in personaje['episodios']):
        print(f"Nombre: {personaje['nombre']}, Episodios: {personaje['episodios']}")

# c. Mostrar toda la información de Darth Vader y Han Solo
cola = Queque()
for p in personajes:
    cola.arrive(p)

print("\n--- c. Información de Darth Vader y Han Solo ---")
while cola.size() > 0:
    personaje = cola.attention()
    if personaje['nombre'] == 'Darth Vader' or personaje['nombre'] == 'Han Solo':
        print(f"\nNombre: {personaje['nombre']}, Altura: {personaje['altura']}, Edad: {personaje['edad']}, Género: {personaje['género']}, "
              f"Especie: {personaje['especie']}, Planeta: {personaje['planeta_natal']}, Episodios: {personaje['episodios']}")

# d. Listar los personajes que aparecen en el episodio VII y en los tres anteriores
cola = Queque()
for p in personajes:
    cola.arrive(p)

print("\n--- d. Personajes que aparecen en el episodio VII y en los episodios 4, 5 o 6 ---")
while cola.size() > 0:
    personaje = cola.attention()
    if 7 in personaje['episodios'] and any(e in [4, 5, 6] for e in personaje['episodios']):
        print(f"Nombre: {personaje['nombre']}, Episodios: {personaje['episodios']}")

# e. Mostrar los personajes con edad mayor a 850 años y de ellos el mayor
cola = Queque()
for p in personajes:
    cola.arrive(p)

mayores_de_850 = []
print("\n--- e. Personajes con edad mayor a 850 años ---")
while cola.size() > 0:
    personaje = cola.attention()
    if personaje['edad'] > 850:
        mayores_de_850.append(personaje)
        print(f"Nombre: {personaje['nombre']}, Edad: {personaje['edad']}")

if mayores_de_850:
    mayor_personaje = max(mayores_de_850, key=lambda p: p['edad'])
    print(f"\nEl personaje más viejo es: {mayor_personaje['nombre']}, con {mayor_personaje['edad']} años")

# f. Eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI
cola = Queque()
for p in personajes:
    cola.arrive(p)

print("\n--- f. Personajes eliminando aquellos que solo aparecieron en episodios IV, V y VI ---")
nuevo_personajes = []
while cola.size() > 0:
    personaje = cola.attention()
    if set(personaje['episodios']) != {4, 5, 6}:
        nuevo_personajes.append(personaje)
        print(f"Nombre: {personaje['nombre']}, Episodios: {personaje['episodios']}")

# g. Listar los personajes de especie humana cuyo planeta de origen es Alderaan
cola = Queque()
for p in personajes:
    cola.arrive(p)

print("\n--- g. Humanos cuyo planeta natal es Alderaan ---")
while cola.size() > 0:
    personaje = cola.attention()
    if personaje['especie'] == 'Humano' and personaje['planeta_natal'] == 'Alderaan':
        print(f"Nombre: {personaje['nombre']}, Planeta Natal: {personaje['planeta_natal']}")

# h. Mostrar toda la información de los personajes cuya altura es menor a 70 centímetros
cola = Queque()
for p in personajes:
    cola.arrive(p)

print("\n--- h. Personajes con altura menor a 70 centímetros ---")
while cola.size() > 0:
    personaje = cola.attention()
    if personaje['altura'] < 70:
        print(f"Nombre: {personaje['nombre']}, Altura: {personaje['altura']}")

# i. Determinar en qué episodios aparece Chewbacca y mostrar además toda su información
cola = Queque()
for p in personajes:
    cola.arrive(p)

print("\n--- i. Información de Chewbacca ---")
while cola.size() > 0:
    personaje = cola.attention()
    if personaje['nombre'] == 'Chewbacca':
        print(f"Nombre: {personaje['nombre']}, Episodios: {personaje['episodios']}")
        print(f"Altura: {personaje['altura']}, Edad: {personaje['edad']}, Especie: {personaje['especie']}, Planeta Natal: {personaje['planeta_natal']}")
