from arbol import BinaryTree

# Suponiendo que tenemos la clase BinaryTree previamente definida, la utilizaremos aquí.
class ExpressionTree(BinaryTree):
    def __init__(self, expression):
        super().__init__()  # Inicializar el árbol binario
        self.build_tree(expression)  # Construir el árbol a partir de la expresión

    def build_tree(self, expression):
        tokens = expression.split()  # Separar la expresión en tokens
        stack = []  # Pila para construir el árbol

        for token in tokens:
            if token.isdigit():  # Si el token es un número
                stack.append(self.__Node(int(token)))  # Crear un nodo hoja
            else:  # Si el token es un operador
                right = stack.pop()  # Sacar el operando derecho
                left = stack.pop()  # Sacar el operando izquierdo
                # Crear un nodo para el operador con los dos operandos como hijos
                new_node = self.__Node(token, left, right)
                stack.append(new_node)  # Agregar el nodo operador a la pila

        self.root = stack.pop()  # La raíz del árbol es el último nodo en la pila

# Ejemplo de uso
expresion = "3 5 + 2 *"  # (3 + 5) * 2
arbol_expresion = ExpressionTree(expresion)

# a. Determinar cuál de los barridos muestra la expresión en el orden correcto
barrido_postorden = []

# Hacer un recorrido en postorden para mostrar la expresión en el orden correcto
def postorden(node):
    if node is not None:
        postorden(node.left)
        postorden(node.right)
        barrido_postorden.append(node.value)

postorden(arbol_expresion.root)
print(f"Postorden (orden correcto de evaluación): {' '.join(map(str, barrido_postorden))}")

# b. Resolver la expresión matemática y mostrar el resultado
def evaluar(node):
    if node is None:
        return 0
    if isinstance(node.value, int):  # Si es un número
        return node.value
    # Si es un operador, se evalúan los hijos
    left_value = evaluar(node.left)
    right_value = evaluar(node.right)
    if node.value == '+':
        return left_value + right_value
    elif node.value == '-':
        return left_value - right_value
    elif node.value == '*':
        return left_value * right_value
    elif node.value == '/':
        return left_value / right_value
    else:
        raise ValueError(f"Operador no soportado: {node.value}")

resultado = evaluar(arbol_expresion.root)
print(f"Resultado de la expresión: {resultado}")
