# Realizar una función recursiva que calcule la potencia de un número:
from Validate import validate_number
def calcular_potencia(base: int, exponente: int) ->int:
    resultado = None
    if validate_number(base):
        if exponente == 0:
            resultado = 1
        else:
            resultado = base * calcular_potencia(base, exponente -1)
    return resultado
