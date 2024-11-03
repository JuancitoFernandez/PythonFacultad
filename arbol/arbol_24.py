import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char: str, freq: int):
        self.char = char  # Carácter
        self.freq = freq  # Frecuencia del carácter
        self.left = None  # Hijo izquierdo
        self.right = None  # Hijo derecho

    def __lt__(self, other):
        # Comparar nodos por frecuencia, y por carácter en caso de empate
        if self.freq == other.freq:
            if self.char is not None and other.char is not None:
                return self.char < other.char
            return self.char is not None  # True si self tiene carácter, False si no
        return self.freq < other.freq

class HuffmanTree:
    def __init__(self):
        self.root = None  # Raíz del árbol

    def construir_arbol(self, frecuencias: dict):
        # Crear una lista de nodos de Huffman
        heap = [HuffmanNode(char, freq) for char, freq in frecuencias.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            izquierda = heapq.heappop(heap)
            derecha = heapq.heappop(heap)

            nodo_padre = HuffmanNode(None, izquierda.freq + derecha.freq)
            nodo_padre.left = izquierda
            nodo_padre.right = derecha

            heapq.heappush(heap, nodo_padre)

        self.root = heap[0]  # La raíz del árbol es el único nodo restante

    def generar_codigos(self):
        codigos = {}
        self._generar_codigos_recursivo(self.root, "", codigos)
        return codigos

    def _generar_codigos_recursivo(self, nodo, codigo_actual, codigos):
        if nodo is not None:
            if nodo.char is not None:  # Es un nodo hoja
                codigos[nodo.char] = codigo_actual
            self._generar_codigos_recursivo(nodo.left, codigo_actual + "0", codigos)
            self._generar_codigos_recursivo(nodo.right, codigo_actual + "1", codigos)

def calcular_frecuencias(texto: str) -> dict:
    return Counter(texto)

def main():
    texto = "este es un ejemplo de texto, para generar un árbol de Huffman."
    frecuencias = calcular_frecuencias(texto)
    print("Frecuencias de caracteres:", frecuencias)

    arbol_huffman = HuffmanTree()
    arbol_huffman.construir_arbol(frecuencias)
    codigos_huffman = arbol_huffman.generar_codigos()

    print("Códigos de Huffman:")
    for char, codigo in codigos_huffman.items():
        print(f"'{char}': {codigo}")

if __name__ == "__main__":
    main()