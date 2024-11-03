from arbol import BinaryTree

# Usando la clase BinaryTree para realizar la actividad
arbol = BinaryTree()

# Insertar nodos de criaturas mitológicas
arbol.insert_node("Talos", other_value={"description": "Un autómata de bronce", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})
arbol.insert_node("Cerbero", other_value={"description": "Perro de tres cabezas que guardaba el inframundo", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})
arbol.insert_node("Toro de Creta", other_value={"description": "Un toro enorme que fue capturado por Heracles", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})
arbol.insert_node("Cierva Cerinea", other_value={"description": "Una cierva mágica", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})
arbol.insert_node("Jabalí de Erimanto", other_value={"description": "Un jabalí gigante", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})
arbol.insert_node("Hidra de Lerna", other_value={"description": "Una serpiente de múltiples cabezas", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})
arbol.insert_node("León de Nemea", other_value={"description": "Un león invulnerable", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})
arbol.insert_node("Quimera", other_value={"description": "Criatura con partes de león, cabra y serpiente", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})
arbol.insert_node("Aves del Estínfalo", other_value={"description": "Aves carnívoras con plumas metálicas", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})
arbol.insert_node("Medusa", other_value={"description": "Criatura con serpientes en la cabeza", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})
arbol.insert_node("Ladón", other_value={"description": "Dragón que custodia las manzanas de oro", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})
arbol.insert_node("Sirenas", other_value={"description": "Criaturas marinas con cantos hipnóticos", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})
arbol.insert_node("Basilisco", other_value={"description": "Un monstruo con mirada mortal", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})
arbol.insert_node("Jabalí de Calidón", other_value={"description": "Jabalí gigante que fue cazado por héroes", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})
arbol.insert_node("Cierva de Cerinea", other_value={"description": "Una cierva mágica", "hero_defeated": "Ninguno", "captured_by": "Ninguno"})

# Actualizar quiénes derrotaron a cada criatura
# Modificaciones de nodos
arbol.search("Cerbero").other_value["hero_defeated"] = "Heracles"
arbol.search("Toro de Creta").other_value["hero_defeated"] = "Heracles"
arbol.search("Cierva Cerinea").other_value["hero_defeated"] = "Heracles"
arbol.search("Jabalí de Erimanto").other_value["hero_defeated"] = "Heracles"
arbol.search("Aves del Estínfalo").other_value["hero_defeated"] = "Heracles"
arbol.search("Cerbero").other_value["captured_by"] = "Heracles"
arbol.search("Toro de Creta").other_value["captured_by"] = "Heracles"
arbol.search("Cierva Cerinea").other_value["captured_by"] = "Heracles"
arbol.search("Jabalí de Erimanto").other_value["captured_by"] = "Heracles"

# Listado inorden de las criaturas y quienes las derrotaron
print("Listado inorden de criaturas y quienes las derrotaron:")
arbol.inorden()

# Mostrar toda la información de la criatura Talos
print("\nInformación de Talos:")
talos_info = arbol.search("Talos")
print(f"Nombre: {talos_info.value}, Descripción: {talos_info.other_value['description']}, Héroe que la derrotó: {talos_info.other_value['hero_defeated']}, Capturada por: {talos_info.other_value['captured_by']}")

# Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
heroes_count = {}
for criatura in ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto", "Aves del Estínfalo"]:
    héroe = arbol.search(criatura).other_value['hero_defeated']
    if héroe != "Ninguno":
        if héroe in heroes_count:
            heroes_count[héroe] += 1
        else:
            heroes_count[héroe] = 1

# Ordenar y mostrar los tres héroes que derrotaron más criaturas
top_heroes = sorted(heroes_count.items(), key=lambda x: x[1], reverse=True)[:3]
print("\nTop 3 héroes que derrotaron criaturas:")
for héroe, cantidad in top_heroes:
    print(f"Héroe: {héroe}, Cantidad de criaturas derrotadas: {cantidad}")

# Listar criaturas derrotadas por Heracles
print("\nCriaturas derrotadas por Heracles:")
for criatura in ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto", "Aves del Estínfalo"]:
    if arbol.search(criatura).other_value['hero_defeated'] == "Heracles":
        print(criatura)

# Listar criaturas que no han sido derrotadas
print("\nCriaturas que no han sido derrotadas:")
for criatura in ["Talos", "Hidra de Lerna", "León de Nemea", "Quimera", "Medusa", "Ladón", "Sirenas", "Basilisco"]:
    if arbol.search(criatura).other_value['hero_defeated'] == "Ninguno":
        print(criatura)

# Eliminar al Basilisco y a las Sirenas
arbol.delete_node("Basilisco")
arbol.delete_node("Sirenas")

# Modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derrotó a varias
arbol.search("Aves del Estínfalo").other_value['hero_defeated'] = "Heracles (derrotó a varias)"

# Modificar el nombre de la criatura Ladón por Dragón Ladón
arbol.search("Ladón").value = "Dragón Ladón"

# Realizar un listado por nivel del árbol
print("\nListado por nivel del árbol:")
arbol.by_level()

# Mostrar las criaturas capturadas por Heracles
print("\nCriaturas capturadas por Heracles:")
for criatura in ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]:
    if arbol.search(criatura).other_value['captured_by'] == "Heracles":
        print(criatura)