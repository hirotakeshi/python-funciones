import datetime

def es_fecha_valida(dia, mes, año):
    try:
  
        fecha = datetime.date(año, mes, dia)
        return True
    except ValueError:
       
        return False

def probar_fecha():
    
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    
    
    if es_fecha_valida(dia, mes, año):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")


probar_fecha()
