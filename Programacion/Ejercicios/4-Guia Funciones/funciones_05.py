# Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
import math

def calcular_area_circulo(radio: float | int | None) -> float | None:
    """Calcula el area de un circulo al ingresar su Radio.

    Args:
        radio (float | int | None): Ingreso del radio del un circulo

    Returns:
        resultado (float | int | None): Devuelve el area del circulo
    """
    resultado = None
    if type(radio) == float or type(radio) == int:
        area = math.pi * radio**2
        resultado = area
    else:
        resultado
    return resultado

nueva_area_circulo = calcular_area_circulo(10)
print(f"El area de el circulo es: {nueva_area_circulo}")