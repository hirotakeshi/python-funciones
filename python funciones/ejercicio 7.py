def lista_cuadrados():
   
    N = int(input("Ingrese el valor de N: "))
    
    
    cuadrados = [x ** 2 for x in range(1, N + 1)]
    
    
    print("Últimos 10 valores de la lista de cuadrados:")
    print(cuadrados[-10:])


lista_cuadrados()
