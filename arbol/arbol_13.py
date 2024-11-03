from arbol_avl import BinaryTree

# Crear el árbol de decisiones
arbol_decision = BinaryTree()
arbol_decision.root = ["¿Es la misión intergaláctica?", None, None]  # Nodo raíz

# Construir el árbol
# Subárbol izquierdo: Sí
arbol_decision.root[1] = ["¿Es necesario ir en equipo?", None, None]
arbol_decision.root[1][1] = ["Guardianes de la Galaxia", None, None]  # Hoja
arbol_decision.root[1][2] = ["Capitana Marvel", None, None]  # Hoja

# Subárbol derecho: No
arbol_decision.root[2] = ["¿Es una misión de recuperación?", None, None]
arbol_decision.root[2][1] = ["¿Es necesario no ser detectado?", None, None]
arbol_decision.root[2][1][1] = ["Ant-Man", None, None]  # Hoja
arbol_decision.root[2][1][2] = ["Black Widow", None, None]  # Hoja

arbol_decision.root[2][2] = ["¿Es una misión de destrucción?", None, None]
arbol_decision.root[2][2][1] = ["Hulk", None, None]  # Hoja
arbol_decision.root[2][2][2] = ["¿Comandará la misión?", None, None]
arbol_decision.root[2][2][2][1] = ["Capitán América", None, None]  # Hoja
arbol_decision.root[2][2][2][2] = ["Doctor Strange", None, None]  # Hoja

# Agregar nodos adicionales
arbol_decision.root[2][2][2][1][1] = ["Spider-Man", None, None]  # Hoja
arbol_decision.root[2][2][2][2][1] = ["Thor", None, None]  # Hoja

# Lógica para determinar el superhéroe asignado
nodo_actual = arbol_decision.root  # Comienza en la raíz

# Bucle para navegar por el árbol
while nodo_actual is not None:
    print(nodo_actual[0])  # Muestra la pregunta actual
    respuesta = input("Respuesta (sí/no): ").strip().lower()  # Solicita la respuesta al usuario
    if respuesta == 'sí':
        nodo_actual = nodo_actual[1]  # Mueve a la izquierda
    elif respuesta == 'no':
        nodo_actual = nodo_actual[2]  # Mueve a la derecha
    else:
        print("Respuesta no válida. Por favor ingresa 'sí' o 'no'.")
        continue  # Vuelve a preguntar si la respuesta es inválida

# Una vez que llega a una hoja, muestra el superhéroe asignado
if nodo_actual is not None:
    print(f"Superhéroe asignado para la misión: {nodo_actual[0]}")
else:
    print("No se ha asignado ningún superhéroe para la misión.")