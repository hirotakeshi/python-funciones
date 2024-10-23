def imprimir_centrada(cadena):
    columnas = 80
   
    espacios = (columnas - len(cadena)) // 2
    
    print(' ' * espacios + cadena)


cadena = input("Ingrese una cadena de caracteres: ")


imprimir_centrada(cadena)
