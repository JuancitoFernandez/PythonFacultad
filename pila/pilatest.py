from pila import Stack
from random import randint

pila = Stack()
pila_aux = Stack()

for i in range(10):
    num = randint(1,99)
    print(num)
    pila.push(num)

while pila.size() > 0:
    data = pila.pop()
    if data % 2 == 0:
        pila_aux.push(data)
    
while pila_aux.size() > 0:
    pila.push(pila_aux.pop())


print( )
print(pila.size())