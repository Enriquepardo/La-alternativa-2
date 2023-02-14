def precio_viaje(num_alumnos, dias):
    # Calculamos el precio del transporte
    transporte = 67.30 if num_alumnos <= 25 else 61.00
    comida = 3.50 * dias_viaje
    # Comprobamos el número de alumnos para calcular el precio del alojamiento
    if num_alumnos < 30:
        alojamiento = 4.75 * num_alumnos*dias
    elif num_alumnos <= 35:
        alojamiento = 4.00 * num_alumnos*dias
    else:
        alojamiento = 3.50 * num_alumnos*dias
    
    precio_total = transporte + comida + alojamiento
    return precio_total


num_alumnos = int(input("Introduce el número de alumnos: "))
dias_viaje = int(input("Introduce el número de días del viaje: "))

print("El precio total del viaje es de", precio_viaje(num_alumnos, dias_viaje), "euros")