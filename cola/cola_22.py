from cola import Queque

# Lista de Jedi
jedi = [
    {'nombre': 'Ahsoka Tano', 'maestros': ['Anakin Skywalker'], 'colores_sable': ['verde', 'blanco'], 'especie': 'Togruta'},
    {'nombre': 'Kit Fisto', 'maestros': ['Mace Windu'], 'colores_sable': ['verde'], 'especie': 'Nautolan'},
    {'nombre': 'Yoda', 'maestros': [], 'colores_sable': ['verde'], 'especie': 'Desconocido'},
    {'nombre': 'Luke Skywalker', 'maestros': ['Yoda', 'Obi-Wan Kenobi'], 'colores_sable': ['azul'], 'especie': 'Humano'},
    {'nombre': 'Mace Windu', 'maestros': ['Yoda'], 'colores_sable': ['violeta'], 'especie': 'Humano'},
    {'nombre': 'Qui-Gon Jinn', 'maestros': [], 'colores_sable': ['verde'], 'especie': 'Humano'},
    {'nombre': 'Obi-Wan Kenobi', 'maestros': ['Qui-Gon Jinn'], 'colores_sable': ['azul'], 'especie': 'Humano'},
    {'nombre': 'Aayla Secura', 'maestros': ['Ki-Adi-Mundi'], 'colores_sable': ['verde'], 'especie': 'Twi\'lek'},
    {'nombre': 'Barriss Offee', 'maestros': ['Luminara Unduli'], 'colores_sable': ['verde'], 'especie': 'Mirialan'},
]

# Crear una cola de Jedi
cola_jedi = Queque()

# Agregar todos los Jedi a la cola
for j in jedi:
    cola_jedi.arrive(j)

# a. Listado ordenado por nombre y especie
print("--- a. Listado ordenado por nombre y especie ---")
jedi_ordenados = []
while cola_jedi.size() > 0:
    jedi_ordenados.append(cola_jedi.attention())

for j in sorted(jedi_ordenados, key=lambda x: (x['nombre'], x['especie'])):
    print(f"Nombre: {j['nombre']}, Especie: {j['especie']}")

# b. Mostrar toda la información de Ahsoka Tano y Kit Fisto
print("\n--- b. Información de Ahsoka Tano y Kit Fisto ---")
for j in jedi_ordenados:
    if j['nombre'] in ['Ahsoka Tano', 'Kit Fisto']:
        print(f"Nombre: {j['nombre']}, Maestros: {j['maestros']}, Colores de sable: {j['colores_sable']}, Especie: {j['especie']}")

# c. Mostrar todos los padawan de Yoda y Luke Skywalker
print("\n--- c. Padawan de Yoda y Luke Skywalker ---")
padawans = []
for j in jedi_ordenados:
    if 'Yoda' in j['maestros'] or 'Luke Skywalker' in j['maestros']:
        padawans.append(j['nombre'])

for padawan in padawans:
    print(f"Padawan: {padawan}")

# d. Mostrar los Jedi de especie humana y Twi'lek
print("\n--- d. Jedi de especie humana y Twi'lek ---")
for j in jedi_ordenados:
    if j['especie'] in ['Humano', "Twi'lek"]:
        print(f"Nombre: {j['nombre']}, Especie: {j['especie']}")

# e. Listar todos los Jedi que comienzan con A
print("\n--- e. Jedi que comienzan con A ---")
for j in jedi_ordenados:
    if j['nombre'].startswith('A'):
        print(f"Nombre: {j['nombre']}")

# f. Mostrar los Jedi que usaron sable de luz de más de un color
print("\n--- f. Jedi que usaron sable de luz de más de un color ---")
for j in jedi_ordenados:
    if len(j['colores_sable']) > 1:
        print(f"Nombre: {j['nombre']}, Colores de sable: {j['colores_sable']}")

# g. Indicar los Jedi que utilizaron sable de luz amarillo o violeta
print("\n--- g. Jedi que utilizaron sable de luz amarillo o violeta ---")
for j in jedi_ordenados:
    if 'amarillo' in j['colores_sable'] or 'violeta' in j['colores_sable']:
        print(f"Nombre: {j['nombre']}, Colores de sable: {j['colores_sable']}")

# h. Indicar los nombres de los padawans de Qui-Gon Jinn y Mace Windu
print("\n--- h. Padawans de Qui-Gon Jinn y Mace Windu ---")
padawans_qui_gon_mace = []
for j in jedi_ordenados:
    if 'Qui-Gon Jinn' in j['maestros'] or 'Mace Windu' in j['maestros']:
        padawans_qui_gon_mace.append(j['nombre'])

for padawan in padawans_qui_gon_mace:
    print(f"Padawan: {padawan}")
