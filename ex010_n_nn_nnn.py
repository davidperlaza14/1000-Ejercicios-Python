# Ejercicio 10: Solicitar al Usuario un Número n y Calcular n + nn + nn

# n = 3 => 3 + 33 + 333 = 369

n = input('Escriba el valor de n: ')

nn = int('{}{}'.format(n, n))
nnn = int('%s%s%s' % (n, n, n))
n = int(n)

suma = n + nn + nnn

print(suma)

# 2 + 22 + 222 = 246