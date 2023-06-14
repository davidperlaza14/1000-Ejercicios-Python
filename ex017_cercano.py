#Python - Ejercicio 17: Crear una Función para Determinar si un Número es Cercano a 1000 o 2000

def cercania(n):

    return (abs(1000 - n) < 100) or (abs(2000 - n) <100)


print(cercania(1000))
print(cercania(950))
print(cercania(200))

print

print(cercania(2000))
print(cercania(1950))
print(cercania(3200))