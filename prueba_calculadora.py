def suma(num_1, num_2):
    resultado = num_1 + num_2
    return resultado

def resta(num_1, num_2):
    resultado = num_1 - num_2
    return resultado

def solicitud():
    solicitud = int(input('Digite el numero: '))
    return solicitud

def menu():
    opcion = int(input("""Digita una de las siguientes opciones:
    1.Suma
    2.Resta
    3.Multiplicacion
    4.Division.
    """))
    return opcion

def decision(opcion):
    num_1 = solicitud()
    num_2 = solicitud()
    if opcion == 1:
        resultado = num_1 + num_2
        opcion = "suma"
    elif opcion == 2:
        resultado = num_1 - num_2
        opcion = "resta"
    elif opcion == 3:
        resultado = num_1 * num_2
        opcion = "multiplicación"
    elif opcion == 4:
        resultado = num_1 / num_2
        opcion = "divición"
    else:
        print(f'Esta {opcion} no esta en el menu ')
    
    print(f'el resultado de la {opcion} es : {resultado} ')

    return resultado

def run():
    opcion = menu()
    decision(opcion)

if __name__ == "__main__":
    run()
    