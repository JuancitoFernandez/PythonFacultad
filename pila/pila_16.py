from pila import Stack

Lista1 = ["Darth Vader", "Luke Skywalker", "Leia Organa", "Obi-Wan Kenobi", "Yoda", "Han Solo", "R2-D2", "Palpatine",
              "C-3PO", "Boba Fett","Chewbacca","Lando Carlissian","Carlist Rieekian","Maximilian Veers","Firmus Piett",
              "Wedge Antilles","Mayor Bren","Bewil","M'Kae","Jabba el Hutt", "Wyren Serper", "Cal Alder", "Toryn Farr",
              "Cecius"]

Lista2 = ["Finn","Han Solo","Kylo Ren","Rey","Leia Organa","C-3PO","Poe Daremon","Luke Skywalker","BB-8",
               "Capitan Phasma","Lider Supremo Snoke","Maz Kanata","General Hux","R2-D2","Chewbacca","Obi-Wan Kenobi",
               "Lor San Tekka","Unkar Plutt","Almirante Ackbar","Bala-Tik","Snap Wexley","Tasu Leech","Yoda","FN-1824",
               "Dr.Kalonia","Thanisson","Unkar Plutt","Jesika Pava","Yolo Siff"]
CapV = Stack()
CapVII = Stack()
Aux = Stack()
Interseccion = Stack()

for i in range(len(Lista1)):
    CapV.push(Lista1[i])
for k in range(len(Lista2)):
    CapVII.push(Lista2[k])

for x in range(CapV.size()):
        personaje1 = CapV.pop()
        for y in range(CapVII.size()):
            personaje2 = CapVII.pop()
            if personaje1 == personaje2:
                Interseccion.push(personaje1)
                print("Interseccion de personajes en ambos capitulos:", personaje1)
            else:
                Aux.push(personaje2)
            if CapVII.size() == 0:
                for O in range(Aux.size()):
                    personaje = Aux.pop()
                    CapVII.push(personaje)


            

        