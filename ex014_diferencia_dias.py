#  Ejercicio 14: Calcular la Diferencia en Días de Dos Fechas Dadas
from datetime import date

hoy = date(1993, 12, 14)
otra_fecha = date(2022, 12, 14)

delta = otra_fecha - hoy

print(delta)
print(delta.days)