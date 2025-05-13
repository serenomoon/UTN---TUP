# Escribir una función parecida a la anterior, pero la misma deberá calcular y 
# devolver el promedio de los números positivos.

def lista_enteros(enteros: list) -> float:
    """Calcula el promedio solo de los numeros enteros positivos

    Args:
        enteros (list): Numeros enteros ingresados

    Returns:
        float: Devuelve un promedio de los numeros positivos
    """
    suma_enteros = 0
    enteros_totales = 0
    total = 0
    for i in range(len(enteros)):
        if enteros[i] > 0:
            suma_enteros += enteros[i]
            enteros_totales += 1
    if enteros_totales != 0:
        total = suma_enteros / enteros_totales

    return total
