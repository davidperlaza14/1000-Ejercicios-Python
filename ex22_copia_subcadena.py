#  Python - Ejercicio 22: Crear una Subcadena de n Caracteres Replicada n Cantidad de Veces

# 'Python', n = 2 => 'Py; 'PyPy'

def replicar_subcadena(cadena, n):
    n_caracteres = n

    if n_caracteres > len(cadena):
        n_caracteres = len(cadena)

    subcadena = cadena[:n_caracteres]

    resultado = ''

    for i in range(n):
        resultado += subcadena
    
    return resultado

print(replicar_subcadena('Python', 2))
print(replicar_subcadena('Python', 5))