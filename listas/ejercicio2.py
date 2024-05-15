
nombre = input(str("ingrese un nombre: "))
vocales = ["a","e","i","o","u"]
lista = []
nombre_final = []

for letra in nombre:
    lista.append(letra)
print(lista)

i= 0
o = 0
while i < len(lista):
    if lista[i] == vocales and o:
        o = 1
    else:   
        nombre_final +=  lista[i]
    i += 1
    
print(nombre)