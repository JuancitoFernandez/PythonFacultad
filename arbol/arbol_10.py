from arbol import BinaryTree

tree = BinaryTree()

def contar_nodos_en_nivel(arbol, nivel):
    def __contar_nodos(root, nivel_actual, nivel_buscado):
        if root is None:
            return 0
        if nivel_actual == nivel_buscado:
            return 1
        else:
            return __contar_nodos(root.left, nivel_actual + 1, nivel_buscado) + \
                   __contar_nodos(root.right, nivel_actual + 1, nivel_buscado)

    return __contar_nodos(arbol.root, 0, nivel)

def analizar_nivel(arbol, nivel):
    nodos_en_nivel = contar_nodos_en_nivel(arbol, nivel)
    nodos_necesarios = 2 ** nivel

    nivel_completo = nodos_en_nivel == nodos_necesarios
    nodos_faltantes = nodos_necesarios - nodos_en_nivel

    return nivel_completo, nodos_faltantes

# Ejemplo de uso
arbol = BinaryTree()
arbol.insert_node(10)
arbol.insert_node(5)
arbol.insert_node(15)
arbol.insert_node(3)
arbol.insert_node(7)
arbol.insert_node(12)
arbol.insert_node(18)

nivel_a_consultar = 6
nodos_en_nivel = contar_nodos_en_nivel(arbol, nivel_a_consultar)
nivel_completo, nodos_faltantes = analizar_nivel(arbol, nivel_a_consultar)

print(f"Nodos en el nivel {nivel_a_consultar}: {nodos_en_nivel}")
print(f"¿El nivel {nivel_a_consultar} está completo? {'Sí' if nivel_completo else 'No'}")
print(f"Nodos faltantes para completar el nivel {nivel_a_consultar}: {nodos_faltantes}")
