
numero_niños = int(input("Escriba el numero de niños: "))


def descuento_parque_warner():
    if numero_niños == 2:
        return 0.10
    elif numero_niños == 3:
        return 0.15
    elif numero_niños == 4:
        return 0.18
    elif numero_niños >= 5:
        return 0.18 + 0.01 * (numero_niños - 4)
    else:
        return 0

print(f'El descuento que tienes es de:', descuento_parque_warner())
