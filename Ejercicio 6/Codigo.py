def descuento(cantidad, cliente):
    descuento = 0
    if cantidad >= 10000 and cantidad <= 20000:
        descuento = 10
    elif cantidad > 20000 and cantidad <= 40000:
        descuento = 15
    elif cantidad > 40000:
        descuento = 20
    if cliente == 'COMMAQ':
        descuento = descuento - 2
    elif cliente == 'BEL':
        descuento = descuento + 1
    return descuento

cantidad = int(input('Ingrese la cantidad de componentes pedidos: '))
cliente = input('Ingrese el nombre del cliente: ')

porcentaje_descuento = descuento(cantidad, cliente)

print('El porcentaje de descuento concedido es:', porcentaje_descuento, '%')
