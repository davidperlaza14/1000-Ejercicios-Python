# Python - Ejercicio 21: Generar los n Primeros Números Pares Positivos

# k mod 2 % == 0 -> k es par

def generar_numeros_pares(n = 100):
    """
    Generar los n Primeros Números Pares Positivos
    """
    pares = []

    contador = 0
    numero = 0

    while contador < n:
        if numero % 2 == 0:
            pares.append(numero)
            contador += 1
        numero += 1
    
    return pares

n = int(input("Escribir la cantidad de numeros pares positivos a generar:  "))

if n > 0:
    pares = generar_numeros_pares(n)

    print(pares)
    print("Cantidad numeros pares: ",len(pares))

else:
    print("El numero debe ser positivo")


