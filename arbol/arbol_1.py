import random
from arbol import BinaryTree

tree = BinaryTree()
for _ in range(1000):
    random_value = random.randint(1, 10000) 
    tree.insert_node(random_value)

# realizar recorrido
print("Pre-order Traversal:")
tree.preorden()
print("\nIn-order Traversal:")
tree.inorden()
print("\nPost-order Traversal:")
tree.postorden()
print("\nLevel-order Traversal:")
tree.by_level()

# Comprobar si un número existe
number_to_search = random.randint(1, 10000)
found_node = tree.search(number_to_search)
print(f"\nSearching for {number_to_search}: {'Found' if found_node else 'Not found'}")

# Eliminar tres nodos aleatorios
for _ in range(3):
    number_to_delete = random.randint(1, 10000)
    delete_result = tree.delete_node(number_to_delete)
    print(f"Deleting {number_to_delete}: {'Deleted' if delete_result else 'Not found in tree'}")

# Calcular alturas de los subárboles izquierdo y derecho
left_height = tree.left_height()
right_height = tree.right_height()
print(f"\nAltura del subárbol izquierdo: {left_height}")
print(f"Altura del subárbol derecho: {right_height}")

# Contar ocurrencias de un elemento específico
element_to_count = random.randint(1, 10000) 
occurrences = tree.search(element_to_count)  
print(f"numero de ocurrencias del elemento {element_to_count}: {occurrences}")

# Contar números pares e impares
even_count = 0
odd_count = 0

def count_even_odd(node):
    global even_count, odd_count
    if node is not None:
        if node.value % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        count_even_odd(node.left)
        count_even_odd(node.right)

count_even_odd(tree.root)
print(f"Números pares: {even_count}")
print(f"Números impares: {odd_count}")