from grafo import Graph

# A- Crear el grafo de personajes de Star Wars
grafo_star_wars = Graph(dirigido=False)

# Cargar personajes
personajes = [
    'Luke Skywalker', 'Darth Vader', 'Yoda', 'Boba Fett', 'C-3PO', 
    'Leia Organa', 'Rey', 'Kylo Ren', 'Chewbacca', 'Han Solo', 'R2-D2', 'BB-8'
]

for personaje in personajes:
    grafo_star_wars.insert_vertice(personaje)

# Agregar aristas con la cantidad de episodios en los que han aparecido juntos
grafo_star_wars.insert_arista("Luke Skywalker", "Leia Organa", 5)
grafo_star_wars.insert_arista("Darth Vader", "Leia Organa", 4)
grafo_star_wars.insert_arista("Leia Organa", "Han Solo", 5)
grafo_star_wars.insert_arista("Han Solo", "Boba Fett", 2)
grafo_star_wars.insert_arista("Yoda", "Luke Skywalker", 2)
grafo_star_wars.insert_arista("Rey", "Finn", 2)  
grafo_star_wars.insert_arista("Rey", "Poe Dameron", 3)  
grafo_star_wars.insert_arista("Chewbacca", "Han Solo", 6)
grafo_star_wars.insert_arista("BB-8", "Poe Dameron", 3)  
grafo_star_wars.insert_arista("C-3PO", "Han Solo", 5)
grafo_star_wars.insert_arista("C-3PO", "Leia Organa", 4)
grafo_star_wars.insert_arista("R2-D2", "C-3PO", 7)  
grafo_star_wars.insert_arista("R2-D2", "Leia Organa", 3) 
grafo_star_wars.insert_arista("Darth Vader", "Boba Fett", 1)  
grafo_star_wars.insert_arista("Boba Fett", "Han Solo", 2)  
grafo_star_wars.insert_arista("Kylo Ren", "Rey", 3)
grafo_star_wars.insert_arista("Kylo Ren", "Han Solo", 2)
grafo_star_wars.insert_arista("Yoda", "Obi-Wan Kenobi", 3) 
grafo_star_wars.insert_arista("Luke Skywalker", "Obi-Wan Kenobi", 3)  

# B- Hallar el árbol de expansión mínima y determinar si contiene a Yoda
def arbol_expansion_minimo_yoda(graph):
    bosque = graph.kruskal("Yoda")  # "Yoda" es solo un punto de partida
    contiene_yoda = any("Yoda" in arbol for arbol in bosque)
    return bosque, contiene_yoda

# Ejecutar funciones
# A- Mostrar el grafo
grafo_star_wars.show_graph()

# B- Hallar el árbol de expansión mínima
bosque, yoda_presente = arbol_expansion_minimo_yoda(grafo_star_wars)
print("Árbol de expansión mínimo contiene a Yoda:", yoda_presente)

# c) Determinar cuál es el número máximo de episodios que comparten dos personajes
def max_episodios_compartidos(graph):
    max_peso = 0
    for nodo in graph.elements:
        for arista in nodo['aristas']:
            if arista['peso'] > max_peso:
                max_peso = arista['peso']
    return max_peso

# Llamar a la función y mostrar el resultado
max_peso = max_episodios_compartidos(grafo_star_wars)
print(f"El número máximo de episodios que comparten dos personajes es: {max_peso}")

def arista_mas_grande(graph):
    max_peso = 0
    nodos = (None, None)  # Inicializa nodos como una tupla vacía
    
    for nodo in graph.elements:
        for arista in nodo['aristas']:
            if arista['peso'] > max_peso:
                max_peso = arista['peso']
                nodos = (nodo['value'], arista['value'])  # Almacena los nodos de la arista más grande
    
    return max_peso, nodos

# Llamar a la función y mostrar el resultado
peso_maximo, nodos_conectados = arista_mas_grande(grafo_star_wars)
print(f"La arista más grande tiene un peso de {peso_maximo} y conecta a los nodos: {nodos_conectados[0]} y {nodos_conectados[1]}")

