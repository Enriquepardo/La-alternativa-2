def calcular_prima_anual(kilometros_recorridos, num_accidentes, antiguedad):
    prima_distancia = min(kilometros_recorridos * 0.01, 400)
    prima_antiguedad = 0
    if antiguedad >= 4:
        prima_antiguedad = 200 + (antiguedad - 4) * 20
    prima = prima_distancia + prima_antiguedad
    if num_accidentes == 0 or (num_accidentes == 1 and prima >= 400):
        return prima
    elif num_accidentes == 1:
        return prima / 2
    elif num_accidentes == 2:
        return prima / 3
    elif num_accidentes == 3:
        return prima / 4
    else:
        return 0