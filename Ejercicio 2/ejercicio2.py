def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        print("Vamos a realizar la comparacion con respecto a la suma y el producto de los mismos")
        funcion_parametro(*args)
        print("Fin de la comparacion")
    return funcion_interior


@funcion_decoradora
def funcion_clasificar(a,b):
    if a*b<a and  a*b<b:
        print(a*b,"<",a,"<",a+b,"<",b)
    elif a<b and a*b>a and a*b<b:
        print(a,"<",a*b,"<",a+b,"<",b)
    elif a<b and a*b>a and a*b<b:
        print(a,"<",a+b,"<",a*b,"<",b)
    else:
        print(a,"<",b,"<",a+b,"<",a*b)


a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))

funcion_clasificar(a,b)