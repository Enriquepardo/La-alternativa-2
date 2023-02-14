def calculate_discount(purchase_amount):
    # Verificar si la cantidad de compra está entre 100 y 500
    if purchase_amount >= 100 and purchase_amount <= 500:
        # Calcular el descuento del 5%
        discount = purchase_amount * 0.05
    # Verificar si la cantidad de compra es mayor que 500
    elif purchase_amount > 500:
        # Calcular el descuento del 8%
        discount = purchase_amount * 0.08
    # Si la cantidad de compra es menor que 100, no hay descuento
    else:
        discount = 0
    # Calcular el importe total después del descuento
    total_amount = purchase_amount - discount
    # Devolver el importe total
    return print(total_amount)


calculate_discount(1000)