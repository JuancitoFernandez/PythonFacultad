class Stack:

    def __init__(self):
        self.__elements = []
#ingresa elementos en la pila
    def push(self, element):
        self.__elements.append(element)
#borrar los ultimos elementos agregados
    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None
#
    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None
#
    def size(self):
        return len(self.__elements)