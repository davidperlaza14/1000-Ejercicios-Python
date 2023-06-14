# Ejercicio 3: Obtener la Fecha y Hora Actuales del Sistema con el Módulo datetime

import datetime

ahora = datetime.datetime.now()
print(ahora)

print(type(ahora))
print(ahora.strftime('%d/%m/%Y %H:%M:%S'))