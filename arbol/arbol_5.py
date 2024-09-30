from arbol import BinaryTree

# 1. Crear el Árbol con Superhéroes y Villanos
mcu_tree = BinaryTree()

# Insertamos personajes (True para superhéroes y False para villanos)
characters = [
    ("Iron Man", True),
    ("Thanos", False),
    ("Captain America", True),
    ("Loki", False),
    ("Spider-Man", True),
    ("Red Skull", False),
    ("Doctor Strange", True),
    ("Ultron", False),
    ("Black Widow", True),
    ("Hela", False)
]

for name, is_hero in characters:
    mcu_tree.insert_node(name, {'is_hero': is_hero})


# 2. Listar los Villanos Ordenados Alfabéticamente (Punto b)
print("Villanos ordenados alfabéticamente:")
mcu_tree.inorden_villanos()


# 3. Mostrar Superhéroes que Empiezan con 'C' (Punto c)
print("\nSuperhéroes que empiezan con 'C':")
mcu_tree.inorden_superheros_start_with('C')


# 4. Determinar Cuántos Superhéroes Hay en el Árbol (Punto d)
num_superheroes = mcu_tree.contar_super_heroes()
print(f"\nNúmero de superhéroes en el árbol: {num_superheroes}")


# 5. Corregir el Nombre de "Doctor Strange" (Punto e)
# Buscamos Doctor Strange y lo corregimos
node = mcu_tree.search("Doctor Strange")
if node is not None:
    node.value = "Dr. Strange"
    print("\nEl nombre ha sido corregido a 'Dr. Strange'")


# 6. Listar Superhéroes en Orden Descendente (Punto f)
def inorden_descendente_heroes(tree):
    def __inorden_descendente(root):
        if root is not None:
            __inorden_descendente(root.right)
            if root.other_value.get('is_hero') is True:
                print(root.value)
            __inorden_descendente(root.left)

    if tree.root is not None:
        __inorden_descendente(tree.root)

print("\nSuperhéroes en orden descendente:")
inorden_descendente_heroes(mcu_tree)


# 7. Crear un Bosque a partir del Árbol (Punto g)
heroes_tree = BinaryTree()
villains_tree = BinaryTree()

def separar_en_bosques(root):
    if root is not None:
        if root.other_value.get('is_hero'):
            heroes_tree.insert_node(root.value, root.other_value)
        else:
            villains_tree.insert_node(root.value, root.other_value)
        separar_en_bosques(root.left)
        separar_en_bosques(root.right)

separar_en_bosques(mcu_tree.root)


# 7.I. Determinar Cuántos Nodos Tiene Cada Árbol (Punto g.I)
def contar_nodos(root):
    if root is None:
        return 0
    return 1 + contar_nodos(root.left) + contar_nodos(root.right)

num_heroes = contar_nodos(heroes_tree.root)
num_villains = contar_nodos(villains_tree.root)

print(f"\nNúmero de nodos en el árbol de héroes: {num_heroes}")
print(f"Número de nodos en el árbol de villanos: {num_villains}")


# 7.II. Barrido Ordenado Alfabéticamente de Cada Árbol (Punto g.II)
print("\nHéroes en orden alfabético:")
heroes_tree.inorden()

print("\nVillanos en orden alfabético:")
villains_tree.inorden()
