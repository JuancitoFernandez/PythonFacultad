from arbol import BinaryTree

# Crear el árbol y añadir nodos
arbol = BinaryTree()
arbol.insert_node(10)
arbol.insert_node(5)
arbol.insert_node(15)
arbol.insert_node(3)
arbol.insert_node(7)
arbol.insert_node(12)
arbol.insert_node(18)

# a. Contar el número de nodos del árbol
total_nodos = 0
pendientes_nodos = [arbol.root]

while pendientes_nodos:
    nodo_actual = pendientes_nodos.pop()
    if nodo_actual is not None:
        total_nodos += 1
        pendientes_nodos.append(nodo_actual.left)
        pendientes_nodos.append(nodo_actual.right)

print(f"Número total de nodos en el árbol: {total_nodos}")

# b. Determinar el número de hojas del árbol
total_hojas = 0
pendientes_hojas = [arbol.root]

while pendientes_hojas:
    nodo_actual = pendientes_hojas.pop()
    if nodo_actual is not None:
        if nodo_actual.left is None and nodo_actual.right is None:
            total_hojas += 1
        pendientes_hojas.append(nodo_actual.left)
        pendientes_hojas.append(nodo_actual.right)

print(f"Número total de hojas en el árbol: {total_hojas}")

# c. Mostrar la información de los nodos hojas
print("Información de los nodos hojas:")
pendientes_mostrar_hojas = [arbol.root]

while pendientes_mostrar_hojas:
    nodo_actual = pendientes_mostrar_hojas.pop()
    if nodo_actual is not None:
        if nodo_actual.left is None and nodo_actual.right is None:
            print(f"Hoja: {nodo_actual.value}")
        pendientes_mostrar_hojas.append(nodo_actual.left)
        pendientes_mostrar_hojas.append(nodo_actual.right)

# d. Determinar el padre de un nodo
valor_a_buscar = 7
padre = None
pendientes_padre = [(arbol.root, None)]  # (nodo_actual, padre_actual)

while pendientes_padre:
    nodo_actual, padre_actual = pendientes_padre.pop()
    if nodo_actual is not None:
        if nodo_actual.value == valor_a_buscar:
            padre = padre_actual
            break
        pendientes_padre.append((nodo_actual.left, nodo_actual))
        pendientes_padre.append((nodo_actual.right, nodo_actual))

if padre:
    print(f"El padre del nodo {valor_a_buscar} es: {padre.value}")
else:
    print(f"El nodo {valor_a_buscar} no tiene padre o no existe.")

# e. Determinar la altura del árbol
altura_arbol = 0
if arbol.root is not None:
    pendientes_altura = [(arbol.root, 1)]  # (nodo_actual, altura_actual)

    while pendientes_altura:
        nodo_actual, altura_actual = pendientes_altura.pop()
        if nodo_actual is not None:
            altura_arbol = max(altura_arbol, altura_actual)
            pendientes_altura.append((nodo_actual.left, altura_actual + 1))
            pendientes_altura.append((nodo_actual.right, altura_actual + 1))

print(f"La altura del árbol es: {altura_arbol}")
