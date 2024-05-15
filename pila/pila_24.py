from pila import Stack

personajes = {"Iron Man":11,"Hulk":9,"Black Widow":9,"Thor":9,"Hawkeye":6,"Capitan America":11,
              "Soldado del Invierno":6,"Falcon":6,"Maquina de Guerra":8,"Quicksilver":2,"Bruja Escarlata":6,
              "Vision":3,"Ant-Man":5,"Avispa":4,"Black Panter":4,"Spider-Man":6,"Dr. Strange":6,"Capitana Marvel":4,
              "Nick Fury":12,"Groot":6,"Rocket Raccoon":6,"Star-Lord":6,"Gamora":5,"Thanos":5}
personaje = ["Iron Man","Hulk","Black Widow","Thor","Hawkeye","Capitan America","Soldado del Invierno","Falcon","Maquina de Guerra","Quicksilver","Bruja Escarlata","Vision","Ant-Man","Avispa","Black Panter","Spider-Man","Dr. Strange","Capitana Marvel","Nick Fury","Groot","Rocket Raccoon","Star-Lord","Gamora","Thanos"]
Pila = Stack()
Aux = Stack()

for i in range(len(personajes)):
    Pila.push(personaje[i])

for j in range(Pila.size()):
        pers = Pila.pop()
        if pers == "Rocket Raccoon":
            print("Rocket Raccoon se encuentra en la posicion: ", j)
        if pers == "Groot":
             print("Groot se encuentra en la posicion: ", j)
        if personajes[pers] > 5:
             print(pers, " aparece en ", personajes[pers], " peliculas de la saga")
        if pers == "Black Widow":
             print("Black Widow (La Viuda Negra), participó en", personajes[pers], " peliculas")
        Aux.push(pers)
while Aux.size() > 0:
    x = Aux.pop()
    Pila.push(x)

for k in range(Pila.size()):
     pers = Pila.pop()
     inicial = pers[0]
     if inicial == "D" or inicial =="G" or inicial == "C":
          print(pers, "comienza con la letra", inicial)
