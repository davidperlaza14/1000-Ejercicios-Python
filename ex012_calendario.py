# Ejercicio 12: Imprimir el Calendario para un Año y Mes Específico

import calendar

agnio = int(input('Escribe el año: '))
mes = int(input('Escriba el mes: '))

print(calendar.month(agnio, mes))