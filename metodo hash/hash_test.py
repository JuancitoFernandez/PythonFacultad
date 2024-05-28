
#def bernstain(cadena):
#    h = 0
#   for caracter in cadena:
#        h = h * 33 + ord(caracter)
#    return h

from random import choice, randint
legiones = ["FL", "TF", "TK", "CT", "FN", "FO",]

tabla_legiones = {}
tabla_numerica = {}

def hash_legion(value):
    return trooper[:2]

def hash_numerica(value):
    return trooper[-3:]

for legion in legiones:
    tabla_legiones[legion] = []

for i in range(0,10):
    trooper = f"{choice(legiones)}-{randint(1000, 9999)}"
    clave = hash_numerica(trooper)
    
    if clave not in tabla_numerica:
        tabla_numerica[clave] = []
    
    tabla_numerica[clave].append(trooper)
    tabla_legiones[hash_legion(trooper)].append(trooper)       

#! FN-2187 es traidor
lista_187 = tabla_numerica.get("187", [])
if "FN-2187" in lista_187:
    print(f"esta en la posicion {pos_fn_2187}")
    print(lista_187)
else:
    print("no esta el trooper")
print()

#! mision de asalto y exploracion
mission_assault = tabla_numerica.get("781", [])
print("atromtroopers para mision de asalto")
for index, trooper in enumerate(mission_assault):
    print(f"{index}-{trooper}")
print()

mission_explore = tabla_numerica.get("537", [])
print("stromtroopers para mision de exporacion")
for index, trooper in enumerate(mission_explore):
    print(f"{index}-{trooper}")
print()

#!
mission_hoth = tabla_numerica.get("537", [])
print("stromtroopers para mision de hoth")
for index, trooper in enumerate(mission_hoth):
    print(f"{index}-{trooper}")
print()


