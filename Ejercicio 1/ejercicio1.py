def sucesor(día):
    dias_de_la_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    indice = dias_de_la_semana.index(día)
    resultado = dias_de_la_semana[(indice + 1) % 7]
    return resultado