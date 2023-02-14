
notas = []
sumanotas  = 0

while True:
    if len(notas) == 4:
        break
    valoresnotas = input("Introduce las 4 notas por separado (nota mínima 0 y máxima 20): ")
    notas.append(int(valoresnotas))


def media():
    global media
    global sumanotas
    for i in range(len(notas)):
        valor = notas[i]
        sumanotas = valor + sumanotas
    media = sumanotas / len(notas)
    print(" \n")
    print("La nota media de las 4 evaluaciones es:", media)

def media_evaluacion(media):
    if media < 12:
        print("El alumno debe reorientarse.")
    elif media > 11 and media < 16:
        print("Alumno con capacidad.")
    elif media > 15 and media <= 20:
        print("Alumno con talento.")

media()
media_evaluacion(media)
