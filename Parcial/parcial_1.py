def imprimir_inverso(lista):
    if lista: 
        print(lista[-1])  
        imprimir_inverso(lista[:-1])
    return lista

#uso de lista inversa
mi_lista = [1, 2, 3, 4, 5]
imprimir_inverso(mi_lista)