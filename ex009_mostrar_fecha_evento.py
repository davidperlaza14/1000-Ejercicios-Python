#  Ejercicio 9: Mostrar la Fecha de un Evento Almacenada en una Tupla

fecha_evento = (2023, 9, 14)

print(type(fecha_evento))

print(fecha_evento)

print('El evento programado sera para la fecha:', fecha_evento)

print('El evento programado sera para la fecha: %i/%i/%i' % fecha_evento)

agnio, mes, dia = fecha_evento
print('El evento programado sera para la fecha: {}/{}/{}'.format(agnio,mes,dia))