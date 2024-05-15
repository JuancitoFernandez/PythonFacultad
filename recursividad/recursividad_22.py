# Actividad 22: Mochila Jedi
def usar_la_fuerza(mochila):
       objetos = 1
       if len(mochila) == 0:
              return " La mochila está vacía, no se encotró un sable de luz. La fuerza no está con Luke esta vez. "
       elif mochila[-1] == "sable de luz":
              return f" Con ayuda de la fuerza, Luke tomó el sable de luz y luchó contra Darth Vader. Solo le tomó retirar {objetos} objetos"
       else:
              objetos += 1
              return usar_la_fuerza(mochila[0:-1])

print(usar_la_fuerza(mochila=["block de hojas","goma de borrar","sable de luz","lapicera", "boligoma"]))