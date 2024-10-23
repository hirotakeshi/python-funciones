def es_capicua(cadena):
    longitud = len(cadena)
    
    
    for i in range(longitud // 2):
        if cadena[i] != cadena[longitud - 1 - i]:
            return False
    return True

def probar_capicua():
   
    cadena = input("Ingrese una cadena de caracteres: ")
    
    
    if es_capicua(cadena):
        print(f"La cadena '{cadena}' es capicúa.")
    else:
        print(f"La cadena '{cadena}' no es capicúa.")


probar_capicua()
