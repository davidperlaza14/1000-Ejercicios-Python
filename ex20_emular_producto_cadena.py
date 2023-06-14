# Python - Ejercicio 20: Emular el Funcionamiento del Producto de Cadenas de Caracteres

def prosucto_cadena(cadena, repeticion):

    resultado = ""

    for i in range(repeticion):
        resultado += cadena
    
    return resultado

print("Python" * 3)
print(prosucto_cadena("Python", 3))