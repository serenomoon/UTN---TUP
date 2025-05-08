# Realizar una función recursiva que calcule la suma de los primeros números naturales:
from Validate import validate_number
def sumar_naturales(numero: int) -> int:
    if validate_number(numero) and numero > 0:
        resultado = numero + sumar_naturales(numero - 1)
    elif numero == 0:
        resultado = 0
    else:
        print("Error, el numero debe ser natural.")
        resultado = None
    return resultado
