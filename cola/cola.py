class Queque:
    
    def __init__(self):
        self.elements = []
        
    def arrive(self, elements):
        self.elements.append(elements)
        
    def attention(self):
        if len(self.elements) > 0:
            return self.elements.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.elements)
    
    def on_font(self):
        if len(self.elements) > 0:
            return self.elements[0]
        else:
            return None
    
    def move_to_end(self):
        element = self.attention()
        if element is not None:
            self.arrive(element)
            
#cola_1 = Queue()

#cola_1.arrive(1)
#cola_1.arrive(2)
#cola_1.arrive(3)
#cola_1.arrive(4)
#cola_1.arrive(5)

#cola_1.attention
#cola_1.attention

#print(cola_1.elements)
#print(cola_1.size())
#print(cola_1.on_font())
#cola_1.move_to_end()
#cola_1.move_to_end()

#para hacer barrido en una lista
#for i in range(cola_1.size()):
#    print(cola_1.on_font())
#    cola_1.move_to_end

#print()
#print(cola_1.size())