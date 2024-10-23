def imprimir_triangulo(filas):
    for i in range(1, filas + 1):
        print('*' * i)

def imprimir_triangulo_invertido(filas):
    for i in range(filas, 0, -1):
        print('*' * i)


def probar_patrones():
    filas = int(input("Ingrese la cantidad de filas: "))
    
    print("Patrón de triángulo:")
    imprimir_triangulo(filas)
    
    print("\nPatrón de triángulo invertido:")
    imprimir_triangulo_invertido(filas)

probar_patrones()
