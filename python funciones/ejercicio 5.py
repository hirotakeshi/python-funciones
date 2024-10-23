cuadrado = lambda x: x ** 2

def probar_lambda():
    
    valor = int(input("Ingrese un número: "))
    
   
    resultado = cuadrado(valor)
    
   
    print(f"El cuadrado de {valor} es {resultado}")


probar_lambda()
