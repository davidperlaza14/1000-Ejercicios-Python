# Ejercicio 7: Obtener el Nombre de Extensión de un Nombre de Archivo

nombre_archivo = input('Ingrese el nombre del archivo: ')

# main.py

partes_nombre_archivo = nombre_archivo.split('.')
print(partes_nombre_archivo)
print(partes_nombre_archivo[-1])
