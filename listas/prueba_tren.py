
lista_de_numeros = [1,20,5,5,67,3,4,-1]

#insertar con posicion
lista_de_numeros.insert(2,99)

#insertar sin posicion
lista_de_numeros.append(123)

#eliminar
try:
    eliminado = lista_de_numeros.remove(101)
except ValueError:
    print("el elemento a eliminar no esta en lista")

if 67 in lista_de_numeros:
    print("eliminar el elemento")
    lista_de_numeros.remove(67)
else:
    print("el elemento a eliminar no esta en lista")
    
#tamaño
print(len(lista_de_numeros))

#ordenar
lista_de_numeros.sort(reverse=True)

#busqueda
try:
    print(f"posicocion", lista_de_numeros.index(20))
except ValueError:
    print("el elemento no se encuentra en la lista")

#barrido
print("listado")
for element in lista_de_numeros:
    print(element)

#print(f"el elemento eliminado es: {eliminado}")