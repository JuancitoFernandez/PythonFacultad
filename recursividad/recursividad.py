def factorialI(numero):
    if numero == 0:
        return 1
    factorial = 1
    for i in range(1, numero+1):
        factorial *= i
    return factorial

def factorialR(numero):
    if numero == 0:
        return 1
    else:
        print(numero)
        return numero * factorialR(numero-1)
    
print(factorialR(5))

#1
def fibonnacci(numero):
    if numero == 0 or numero ==1:
        return numero
    else:
        return fibonnacci(numero-1) + fibonnacci(numero-2)

def fibonacci_inter(numero):
    if numero == 0 or numero ==1:
        return numero
    else:
        fibn_1 = 1
        fibn_2 = 0
        for i in range(2,numero + 1):
            fibn_2, fibn_1 = fibn_1, fibn_1 + fibn_2
        return fibn_1
        
#6
def invertir_cadena(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])
    
cadena = "hola mundo"
print(invertir_cadena(cadena))

#7
def sumatoria_serie(numero):
    if numero == 1:
        return 1
    else:
        return 1/numero + sumatoria_serie(numero-1)
    
print(sumatoria_serie(2))

#8
def convertir_binario(numero):
    if numero <= 1:
        return str(numero)
    else:
        return convertir_binario(numero//2) + str(numero % 2)
    
print(convertir_binario(2))

#10
def cantidad_digitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + cantidad_digitos(numero // 10)
    
print(cantidad_digitos(123))

#11
def invertir_numero(numero):
    if numero < 10:
        return numero
    else:
        return (numero % 10) * 10 ** cantidad_digitos(numero//10) + invertir_numero(numero // 10)

print(invertir_numero(12345678))

#14
def sumar_digitos(numero):
    if numero < 10:
        return numero
    else:
        return (numero % 10) + sumar_digitos(numero // 10)

print(sumar_digitos(9))

#15
def raiz_aux(numero_calcular, valor=2):
    if numero_calcular == 0 or numero_calcular == 1:
        return numero_calcular
    else:
        resultado = valor * valor
        if resultado == numero_calcular:
            return valor
        elif resultado > numero_calcular:
            return valor -1
        else:
            return raiz_aux(numero_calcular, valor + 1)
        
print(raiz_aux(4))
       
#17
nombres = ["juan", "lucila", "cami"]
def barridos(lista):
    if len(lista) == 1:
        print(lista[0])
    else:
        print(lista[-1])
        barridos(lista[:-1])

print(barridos(nombres))