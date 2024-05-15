# Actividad 5: convertir numeros romanos a decimales
def romano_a_dec(rom):
    romanos = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    if len(rom) == 1:
          return romanos[rom]
    elif  romanos[rom[-2]] != None and romanos[rom[-2]] < romanos[rom[1]]:
            return romano_a_dec(rom[1]) - romanos[rom[:-1]] 
    else:
            return romanos[rom[1]] + romano_a_dec(rom[:-1])
    
    
print(romano_a_dec("XX"))