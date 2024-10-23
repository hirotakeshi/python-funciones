es_par = lambda x: x % 2 == 0

def probar_lambda_paridad():
    
    valor = int(input("Ingrese un número: "))
    
    
    if es_par(valor):
        print(f"El número {valor} es par.")
    else:
        print(f"El número {valor} es impar.")


probar_lambda_paridad()
