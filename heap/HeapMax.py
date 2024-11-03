class Pedido:
    def __init__(self, general: str, planeta: str, descripcion: str):
        self.general = general
        self.planeta = planeta
        self.descripcion = descripcion

    def __repr__(self):
        return f"Pedido(general='{self.general}', planeta='{self.planeta}', descripcion='{self.descripcion}')"

class HeapMax:
    def __init__(self):
        self.elements = []

    def add(self, value):
        self.elements.append(value)
        self.float(len(self.elements) - 1)

    def remove(self):
        if len(self.elements) > 0:
            self.interchange(0, len(self.elements) - 1)
            value = self.elements.pop()
            self.sink(0)
            return value
        else:
            return None

    def interchange(self, index_1, index_2):
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def float(self, index):
        father = (index - 1) // 2
        while index > 0 and self.elements[index][0] > self.elements[father][0]:  # Comparar prioridades
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index):
        left_child = (index * 2) + 1
        control = True
        while control and left_child < len(self.elements):
            right_child = (index * 2) + 2
            max = left_child
            if right_child < len(self.elements):
                if self.elements[right_child][0] > self.elements[left_child][0]:  # Comparar prioridades
                    max = right_child
            if self.elements[index][0] < self.elements[max][0]:  # Comparar prioridades
                self.interchange(index, max)
                index = max
                left_child = (index * 2) + 1
            else:
                control = False

    def arrive(self, value, priority):
        self.add((priority, value))  # Almacenar como tupla (prioridad, Pedido)

    def atention(self):
        return self.remove()